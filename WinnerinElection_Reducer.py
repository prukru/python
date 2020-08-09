#!/usr/bin/python
import sys

candidatevotedic = dict()

# if i need to test it myself without being read from stdin for debugging.
#
# lines = '''Trump\t1
# Trump\t1
# Trump\t1
# Biden\t1
# Biden\t1
# Trump\t1'''
#
# lines = lines.split('\n')

# input comes from STDIN
lines = sys.stdin

for line in lines:
    # remove leading and trailing whitespace
    line = line.strip()
    candidatename, votecount = line.split('\t')
    # convert count (currently a string) to int
    try:
        votecount = int(votecount)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # string comprehend , get the count against a key , if not found then 0 , so add + 1 whatever it returns
    candidatevotedic[candidatename] = candidatevotedic.get(candidatename, 0) + 1

max_vote_frequencey = 0
winner_candidate = ''

for k,v in candidatevotedic.items() :
    if v > max_vote_frequencey :
        max_vote_frequencey = v
        winner_candidate = k
print('Winner is : {0} with votes {1}'.format(winner_candidate, max_vote_frequencey))
