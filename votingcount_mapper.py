#! /usr/bin/env python

import sys

infile= sys.stdin

# Remove the header line
#next(infile)

for line in infile:
    line = line.strip()
    unpacked = line.split("|")
    ID, State, Candidate  = line.split("|")
    results = [Candidate, "1"]
    print("\t".join(results))
