#!/usr/bin/env python3

import sys
from collections import Counter

def usage():
    print("Usage: python simple_log_parser.py <logfile> <keyword1> [keyword2] [...]")
    sys.exit(1)

if len(sys.argv) < 3:
    usage()

log_file = sys.argv[1]
keywords = [k.lower() for k in sys.argv[2:]]

counts = Counter({k: 0 for k in keywords})

with open(log_file, "r", errors="ignore") as f:
    for line in f:
        lower_line = line.lower()
        for k in keywords:
            if k in lower_line:
                counts[k] += 1

print(f"Results for {log_file}:")
for k in keywords:
    print(f"{k}: {counts[k]} occurrences")
