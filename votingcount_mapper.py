#! /usr/bin/env python

import sys

infile= sys.stdin

#split the input line and start separating candidate column only
for line in infile:
    line = line.strip()
    unpacked = line.split("|")
    ID, State, Candidate  = line.split("|")
    results = [Candidate, "1"]
    print("\t".join(results))
