#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=2426

# Given an array of 1001 elements which contains integers from 1 to 1000 inclusive.
# The numbers are randomly stored in the array. Only one number repeats itself. The
# candidate has to come up with an efficient solution for finding that duplicate
# given that you can access the elements of an array only once i.e., you can read
# the elements of the array only once.

# Lets make that a bit more interesting shall we. 

# First create the array randomly and the one number randomly. But use 10 million
# integers plus one of course. Do this 10 times and show the times it takes to find
# the number and then the average time. Fastest wins.

import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 1:
        print "Usage: python find_dupe.py numElements".format(len(argv[1:]))
        exit(-1)
    numElements = int(argv[1])
    

if __name__ == "__main__":
    sys.exit(main())
