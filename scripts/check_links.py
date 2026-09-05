#!/usr/bin/env python3
"""Verify every internal link in a built Hugo site resolves to a real file.

Hugo does not validate internal links. A renamed post or a mistyped wiki path
404s silently in production. This walks the built HTML and resolves every
site-relative href/src against the output directory.
"""
import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.I)
SKIP_SCHEME = re.compile(r'^(?:[a-z][a-z0-9+.-]*:|//|#)', re.I)


def resolve(root: Path, url: str) -> bool:
    """True if a site-relative URL maps to a file Hugo actually emitted."""
    path = unquote(urlsplit(url).path)
    if not path or path == "/":
        return (root / "index.html").exists()
    target = root / path.lstrip("/")
    if path.endswith("/"):
        return (target / "index.html").exists()
    return target.is_file() or (target / "index.html").exists()


def check(root: Path, other: Path | None = None) -> list[str]:
    """Report links that do not resolve in `root`.

    When `other` is given (a build that includes drafts), a target that exists
    there but not here is a link to an unpublished page: it resolves locally and
    404s in production. That needs publishing the post or dropping the link, not
    fixing a typo, so it is reported as its own kind of failure.
    """
    if not root.is_dir():
        sys.exit(f"check_links: no such build directory: {root}")
    failures = []
    for page in sorted(root.rglob("*.html")):
        source = "/" + str(page.relative_to(root).parent).replace("\\", "/").strip(".") + "/"
        for raw in LINK.findall(page.read_text(encoding="utf-8", errors="replace")):
            url = html.unescape(raw).strip()
            if not url or SKIP_SCHEME.match(url) or not url.startswith("/"):
                continue
            if resolve(root, url):
                continue
            if other is not None and resolve(other, url):
                label = "links to a DRAFT page (404s in production)"
            else:
                label = "broken link (no such page)"
            failures.append(f"  {label}\n      {url}\n      linked from {source}")
    return failures


def main() -> int:
    if len(sys.argv) != 3:
        sys.exit("usage: check_links.py <build-with-drafts> <build-without-drafts>")
    drafts, published = (Path(a) for a in sys.argv[1:3])

    # Pass 1: every link, drafts included. Catches typos before an article ships.
    # Pass 2: published pages only, so a live page pointing at an unpublished one
    # is caught -- it resolves under --buildDrafts and 404s on nytime5.com.
    failures = check(drafts) + check(published, other=drafts)
    if failures:
        print(f"FAIL  {len(failures)} unresolved internal link(s):\n", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
        return 1

    pages = sum(1 for _ in drafts.rglob("*.html"))
    print(f"OK    internal links resolve across {pages} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
