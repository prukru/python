#! /usr/bin/python

import sys

#input comes from STDIN (standard input)

for line in sys.stdin:
        line = line.strip()
        unpacked = line.split("|")
        ID, State, Candidate = line.split("|")


        results = [State+'-'+Candidate,"1"]
        print("|".join(results))
