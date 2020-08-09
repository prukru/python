#!/usr/bin/python
import sys

# if i need to test it myself without being read from stdin for debugging.

# lines = '''991981297|Utah|Trump
# 72945457|Colorado|Trump
# 813347603|Utah|Biden
# 654728434|Kansas|Biden
# 229007354|Oklahoma|Biden
# 53517064|Alaska|Biden
# 750338354|Maine|Biden
# 565984821|Tennessee|Trump
# 31304895|Michigan|Biden
# 137608301|Virginia|Trump
# 402311094|Florida|Trump
# 347954883|Louisiana|Trump'''
#lines = lines.split('\n')

#input comes from STDIN (standard input)
lines = sys.stdin

for line in lines:
    line = line.strip()
    voteid, region, candidatename = line.split("|")
    results = [candidatename, "1"]
    print("\t".join(results))
