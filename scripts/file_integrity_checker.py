#!/usr/bin/env python3

import hashlib
import sys

def usage():
    print("Usage: python file_integrity_checker.py <file> <expected_hash>")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

file_path = sys.argv[1]
expected_hash = sys.argv[2].lower()

def sha256_hash(filename):
    sha256 = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)

calculated_hash = sha256_hash(file_path)

print(f"\nCalculated Hash: {calculated_hash}")
print(f"Expected Hash:   {expected_hash}")

if calculated_hash == expected_hash:
    print("\n✅ File integrity verified — hashes match.")
else:
    print("\n❌ WARNING: File has been modified or corrupted.")
