#! /usr/bin/python

import sys

last_State = None
Vote_count = 0


for line in sys.stdin:

        line = line.strip()
        State, count = line.split("|")
        count = int(count)


        #For 1st iteration

        if not last_State:
                last_State = State


        #if they are same state, count the votes

        if State.strip() == last_State.strip():
                Vote_count += count
        else:
                result = [last_State, Vote_count]


                if Vote_count > 1:
                        print("|".join(str(v) for v in result))
                last_State = State
                Vote_count = 1


# this is to catch the final value we output

print("|".join(str(v) for v in [last_State,Vote_count]))
