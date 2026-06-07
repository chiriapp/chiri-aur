#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 2:
    print("Usage: ./update.py <version> (e.g., 0.9.0)")
    sys.exit(1)

version = sys.argv[1].lstrip('v')
print(f"Updating package to v{version}...")

def update_file(filepath, replacements):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        for pattern, repl in replacements:
            content = re.sub(pattern, repl, content, flags=re.MULTILINE)
        with open(filepath, 'w') as f:
            f.write(content)
    except FileNotFoundError:
        print(f"File not found: {filepath}")

update_file("PKGBUILD", [
    (r"^pkgver=.*", f"pkgver={version}"),
    (r"^pkgrel=.*", "pkgrel=1")
])
update_file(".SRCINFO", [
    (r"^\s*pkgver = .*", f"\tpkgver = {version}"),
    (r"^\s*pkgrel = .*", "\tpkgrel = 1")
])

print("==> Done!")
