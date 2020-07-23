#! /usr/bin/env python

import sys

last_Candidate = None
Vote_count = 0

for line in sys.stdin:

    line = line.strip()
    Candidate, count = line.split("\t")

    count = int(count)
    # if this is the first iteration
    if not last_Candidate:
        last_Candidate = Candidate

    # if they're the same, count the votes
    if Candidate.strip() == last_Candidate.strip():
        Vote_count += count
    else:

        result = [last_Candidate, Vote_count]

        if Vote_count > 1:
           print("\t".join(str(v) for v in result))
        last_Candidate = Candidate
        Vote_count = 1

# this is for the display of  the final value that we output
print("\t".join(str(v) for v in [last_Candidate, Vote_count]))
