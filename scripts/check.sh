#!/usr/bin/env bash
# The definition of done for nytime5. Must pass before any deploy.
#
#   1. The site builds, drafts included.
#   2. Every internal link resolves -- Hugo will not tell you when one does not.
#
# Do not weaken this check to make a build pass.
set -euo pipefail

cd "$(dirname "$0")/.."

OUT=".check"
trap 'rm -rf "$OUT"' EXIT
rm -rf "$OUT"

echo "==> building (with drafts)"
npx hugo --buildDrafts --destination "$OUT/drafts" --quiet

echo "==> building (published only)"
npx hugo --destination "$OUT/published" --quiet

echo "==> checking internal links"
python3 scripts/check_links.py "$OUT/drafts" "$OUT/published"

echo
echo "PASS"
