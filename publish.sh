#!/usr/bin/env bash
# Publish the already-validated v1.3 website to the existing main branch.
# Requires git + Python 3 and push authentication for the GitHub account.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REMOTE="${BHG_REMOTE:-https://github.com/pkugelmann/born-hopf-geometry.git}"
BRANCH="${BHG_BRANCH:-main}"
DRY_RUN=0
if [[ "${1:-}" == "--dry-run" ]]; then DRY_RUN=1; elif [[ $# -gt 0 ]]; then echo 'Usage: bash publish.sh [--dry-run]' >&2;exit 2;fi
command -v git >/dev/null || { echo 'Install Git first.' >&2;exit 1; }
command -v python3 >/dev/null || { echo 'Install Python 3 first.' >&2;exit 1; }
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
REPO="$TMP/repo"
printf 'Cloning the existing repository from %s...\n' "$REMOTE"
git clone --depth 1 --branch "$BRANCH" --single-branch "$REMOTE" "$REPO"
printf 'Applying website package; unrelated files and Git history are preserved...\n'
python3 "$HERE/scripts/apply_release.py" "$HERE" "$REPO"
python3 "$REPO/scripts/check_site.py"
git -C "$REPO" add -A
# Lint only maintained website/editorial code. The imported primary .tex/.csv,
# historical audits and exact diagrams intentionally remain byte-for-byte
# identical to the released archives, including any original whitespace.
git -C "$REPO" diff --cached --check -- . \
  ':(exclude)docs/manuscripts/**' \
  ':(exclude)docs/verification/**' \
  ':(exclude)docs/geometry/**' \
  ':(exclude)content/protocols/**'
printf '\nChanges being prepared:\n'
git -C "$REPO" diff --cached --stat | tail -n 32
if git -C "$REPO" diff --cached --quiet; then
  echo 'No differences; the remote repository already contains this package.'
  exit 0
fi
if [[ "$DRY_RUN" == 1 ]]; then
  printf '\nDRY RUN COMPLETE: No commit or push was performed.\n'
  exit 0
fi
printf '\nCommitting and pushing to %s...\n' "$BRANCH"
git -C "$REPO" commit -m 'Update Born–Hopf site v1.3; sync Papers v3.077, Audits v1.83, DAG v1.323, S³ v1.49'
git -C "$REPO" push origin "$BRANCH"
printf '\nPUSHED. Check GitHub Actions and Settings > Pages (source: GitHub Actions).\n'
printf 'Repository: https://github.com/pkugelmann/born-hopf-geometry\n'
printf 'Expected website after deployment: https://pkugelmann.github.io/born-hopf-geometry/\n'
