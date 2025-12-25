#!/bin/sh
set -e

# Locate tourmaline.py by searching script dir and parent directories (up to 6 levels)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SEARCH_DIR="$SCRIPT_DIR"
FOUND=""
i=0
while [ $i -lt 6 ]; do
  if [ -f "$SEARCH_DIR/tourmaline.py" ]; then
    FOUND="$SEARCH_DIR/tourmaline.py"
    break
  fi
  SEARCH_DIR="$(dirname "$SEARCH_DIR")"
  i=$((i + 1))
done

# If there's an installed entry point called 'tourmaline', use it
if [ -z "$FOUND" ] && command -v tourmaline >/dev/null 2>&1; then
  exec tourmaline "$@"
fi

# Fallback: search common locations quickly
if [ -z "$FOUND" ]; then
  FOUND="$(find "$HOME" /usr/local /opt 2>/dev/null -type f -name 'tourmaline.py' -print -quit || true)"
fi

if [ -z "$FOUND" ]; then
  echo "Error: could not find 'tourmaline.py' (checked script parents, PATH and common locations)."
  exit 1
fi

exec python3 "$FOUND" "$@"