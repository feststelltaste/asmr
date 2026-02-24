#!/usr/bin/env python3
"""
Link checker for the ASMR practices.

For every Markdown link in _practices/*.md:
  - Fetch the URL and report the HTTP status.
  - For YouTube URLs additionally:
      * Detect "This video isn't available anymore" in the page source.
      * Compare the link-text title used in the Markdown to the actual
        video title fetched from YouTube (og:title / <title>), and
        warn if they differ significantly.

Usage:
    python check_links.py [--practices-dir PATH] [--timeout SECONDS]
"""

import argparse
import difflib
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
PRACTICES_DIR = Path(__file__).parent / "_practices"
REQUEST_TIMEOUT = 10          # seconds per request
YOUTUBE_TITLE_THRESHOLD = 0.4  # SequenceMatcher ratio below which we warn
DELAY_BETWEEN_REQUESTS = 0.5  # seconds — be polite to servers

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; link-checker/1.0; "
        "+https://github.com/your-repo)"
    )
}

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class LinkResult:
    file: str
    link_text: str
    url: str
    status: Optional[int] = None
    error: Optional[str] = None
    # YouTube-specific
    yt_unavailable: bool = False
    yt_actual_title: Optional[str] = None
    yt_title_ratio: Optional[float] = None
    yt_title_warn: bool = False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
MARKDOWN_LINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^\s\)]+)\)')

def extract_links(md_text: str) -> list[tuple[str, str]]:
    """Return list of (link_text, url) from a Markdown string."""
    return MARKDOWN_LINK_RE.findall(md_text)


YOUTUBE_RE = re.compile(
    r'https?://(?:www\.)?(?:youtube\.com/watch\?[^\s\)]*v=|youtu\.be/)[\w-]+'
)

def is_youtube(url: str) -> bool:
    return bool(YOUTUBE_RE.match(url))


def fetch(url: str, timeout: int) -> tuple[Optional[int], Optional[str], Optional[bytes]]:
    """
    Fetch a URL.  Returns (status_code, error_message, body_bytes).
    body_bytes is None on error or for non-YouTube requests.
    """
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return resp.status, None, body
    except urllib.error.HTTPError as exc:
        return exc.code, str(exc), None
    except urllib.error.URLError as exc:
        return None, str(exc.reason), None
    except Exception as exc:  # noqa: BLE001
        return None, str(exc), None


def extract_yt_title(html: bytes) -> Optional[str]:
    """
    Extract the video title from a YouTube HTML page.
    Tries og:title first (most reliable in static HTML), then <title>.
    """
    text = html.decode("utf-8", errors="replace")

    # og:title  — e.g.  <meta property="og:title" content="My Video Title">
    og = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', text)
    if og:
        return og.group(1)

    # <title>My Video Title - YouTube</title>
    title_tag = re.search(r'<title>(.*?)</title>', text)
    if title_tag:
        t = title_tag.group(1)
        t = re.sub(r'\s*-\s*YouTube\s*$', '', t, flags=re.IGNORECASE)
        return t.strip() or None

    return None


def title_similarity(a: str, b: str) -> float:
    """SequenceMatcher ratio after lower-casing and stripping punctuation."""
    def normalise(s: str) -> str:
        return re.sub(r'[^\w\s]', '', s.lower())
    return difflib.SequenceMatcher(None, normalise(a), normalise(b)).ratio()


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------
def check_link(link_text: str, url: str, timeout: int) -> LinkResult:
    result = LinkResult(file="", link_text=link_text, url=url)

    youtube = is_youtube(url)
    # For YouTube we only need the status code from the watch page; titles come via oEmbed
    status, error, body = fetch(url, timeout if not youtube else timeout)
    result.status = status
    result.error = error

    if youtube:
        # Use the oEmbed API — works without JS rendering or consent pages.
        # A 404 from oEmbed means the video is deleted/private.
        vid_id = re.search(r'(?:v=|youtu\.be/)([\w-]+)', url)
        if vid_id:
            oembed_url = (
                f"https://www.youtube.com/oembed"
                f"?url=https://www.youtube.com/watch?v={vid_id.group(1)}&format=json"
            )
            oe_status, oe_error, oe_body = fetch(oembed_url, timeout)
            if oe_status == 404:
                result.yt_unavailable = True
            elif oe_body:
                import json as _json
                try:
                    oe_data = _json.loads(oe_body)
                    actual_title = oe_data.get("title")
                    result.yt_actual_title = actual_title
                    if actual_title:
                        ratio = title_similarity(link_text, actual_title)
                        result.yt_title_ratio = ratio
                        result.yt_title_warn = ratio < YOUTUBE_TITLE_THRESHOLD
                except Exception:
                    pass

    return result


def check_all_practices(practices_dir: Path, timeout: int) -> list[LinkResult]:
    results: list[LinkResult] = []
    seen_urls: dict[str, LinkResult] = {}  # url -> first result (reuse fetched data)

    md_files = sorted(practices_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {practices_dir}", file=sys.stderr)
        return results

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        links = extract_links(content)

        for link_text, url in links:
            # Strip trailing punctuation that sometimes leaks into the URL
            url = url.rstrip('.,;:')

            if url in seen_urls:
                # Reuse status/body info but record the new link_text + file
                prev = seen_urls[url]
                r = LinkResult(
                    file=md_file.name,
                    link_text=link_text,
                    url=url,
                    status=prev.status,
                    error=prev.error,
                    yt_unavailable=prev.yt_unavailable,
                    yt_actual_title=prev.yt_actual_title,
                )
                if r.yt_actual_title:
                    ratio = title_similarity(link_text, r.yt_actual_title)
                    r.yt_title_ratio = ratio
                    r.yt_title_warn = ratio < YOUTUBE_TITLE_THRESHOLD
                r.file = md_file.name
                results.append(r)
                continue

            print(f"  Checking {url[:80]}...", end=" ", flush=True)
            r = check_link(link_text, url, timeout)
            r.file = md_file.name
            seen_urls[url] = r
            results.append(r)

            status_str = str(r.status) if r.status else "ERR"
            print(status_str)

            time.sleep(DELAY_BETWEEN_REQUESTS)

    return results


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
RESET  = "\033[0m"
RED    = "\033[31m"
YELLOW = "\033[33m"
GREEN  = "\033[32m"
BOLD   = "\033[1m"
CYAN   = "\033[36m"


def colour(text: str, code: str) -> str:
    return f"{code}{text}{RESET}"


def print_report(results: list[LinkResult]) -> int:
    """Print a human-readable report.  Returns exit code (0 = all ok)."""
    # 403 Forbidden is often bot-blocking, not a dead page — treat as warning only
    def is_error(r: LinkResult) -> bool:
        if r.status == 403:
            return False
        return bool(r.error or (r.status and r.status >= 400) or r.yt_unavailable or r.yt_title_warn)

    errors   = [r for r in results if is_error(r)]
    warnings = [r for r in results if r.status == 403]
    issues   = errors + warnings

    print()
    print(colour("=" * 70, BOLD))
    print(colour("  LINK CHECK REPORT", BOLD))
    print(colour("=" * 70, BOLD))
    print(f"  Total links checked : {len(results)}")
    print(f"  Errors              : {len(errors)}")
    print(f"  Warnings (403)      : {len(warnings)}")
    print(colour("=" * 70, BOLD))

    if not issues:
        print(colour("\n  All links look good!", GREEN))
        return 0

    if not errors:
        print(colour("\n  No broken links. Review warnings above.", YELLOW))

    # Group by file for readability
    by_file: dict[str, list[LinkResult]] = {}
    for r in issues:
        by_file.setdefault(r.file, []).append(r)

    for fname, file_issues in sorted(by_file.items()):
        print(f"\n{colour(fname, BOLD + CYAN)}")
        for r in file_issues:
            print(f"  [{r.link_text[:60]}]")
            print(f"  {r.url}")

            if r.error:
                print(f"    {colour('ERROR', RED)}: {r.error}")
            elif r.status == 403:
                print(f"    {colour('HTTP 403 (bot-blocked, verify manually)', YELLOW)}")
            elif r.status and r.status >= 400:
                print(f"    {colour(f'HTTP {r.status}', RED)}")
            else:
                print(f"    HTTP {r.status}")

            if r.yt_unavailable:
                print(f"    {colour('YouTube: video is unavailable', RED)}")

            if r.yt_title_warn:
                ratio_pct = f"{r.yt_title_ratio * 100:.0f}%"
                print(
                    f"    {colour('YouTube title mismatch', YELLOW)} "
                    f"(similarity {ratio_pct})"
                )
                print(f"      Markdown : {r.link_text[:80]}")
                print(f"      Actual   : {r.yt_actual_title}")
            elif r.yt_actual_title:
                ratio_pct = f"{r.yt_title_ratio * 100:.0f}%"
                print(
                    f"    {colour('YouTube title ok', GREEN)} "
                    f"(similarity {ratio_pct}): {r.yt_actual_title[:60]}"
                )
            print()

    return 1 if errors else 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--practices-dir",
        type=Path,
        default=PRACTICES_DIR,
        help=f"Path to _practices directory (default: {PRACTICES_DIR})",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=REQUEST_TIMEOUT,
        help=f"Request timeout in seconds (default: {REQUEST_TIMEOUT})",
    )
    args = parser.parse_args()

    print(colour(f"Scanning {args.practices_dir} ...\n", BOLD))
    results = check_all_practices(args.practices_dir, args.timeout)
    exit_code = print_report(results)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
