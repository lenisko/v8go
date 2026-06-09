#!/usr/bin/env python3
"""Resolve the build-engine input to a V8 git commit + release tag and emit
GitHub Actions outputs (v8_hash, chrome_major, chrome_version, tag).

Input may be: a 40-hex V8 commit; a Chrome major (e.g. 148); or "latest".
Usage: resolve-v8.py <commit|chrome-major|latest>
"""
import json
import os
import re
import sys
import urllib.request


def emit(key: str, val: str) -> None:
    """Print key=val and append to $GITHUB_OUTPUT when set."""
    line = f"{key}={val}"
    print(line)
    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def main() -> None:
    """Resolve the input and emit the build outputs."""
    inp = (sys.argv[1] if len(sys.argv) > 1 else "latest").strip()
    if re.fullmatch(r"[0-9a-fA-F]{40}", inp):
        emit("v8_hash", inp)
        emit("chrome_major", "")
        emit("chrome_version", "")
        emit("tag", f"engine-{inp[:12]}")
        return
    num = 1 if inp == "latest" else 80
    url = (
        "https://chromiumdash.appspot.com/fetch_releases"
        f"?channel=Stable&platform=Mac&num={num}"
    )
    with urllib.request.urlopen(url, timeout=30) as resp:  # trusted host
        data = json.load(resp)
    if inp == "latest":
        entry = data[0]
    else:
        major = int(inp)
        cands = [d for d in data if d.get("milestone") == major]
        cands.sort(key=lambda d: d.get("time", 0), reverse=True)
        if not cands:
            sys.exit(f"no Stable release found for Chrome {inp}")
        entry = cands[0]
    v8_hash = entry["hashes"]["v8"]
    chrome_major = str(entry.get("milestone", ""))
    emit("v8_hash", v8_hash)
    emit("chrome_major", chrome_major)
    emit("chrome_version", entry.get("version", ""))
    emit("tag", f"engine-chrome{chrome_major}")


if __name__ == "__main__":
    main()
