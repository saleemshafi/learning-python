#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=2055

# This weeks puzzle is a nice and simple one to ease all those with sore heads
# from the July 4th celebrations back into thinking code...
#
# If you've read the Dan Brown book "The Da Vinci Code" then you'll be quite
# familiar with this already... we would like you to calculate 'X' numbers in
# the Fibonacci Sequence, which is essentially adding the previous 2 occurring
# numbers together to make the next .. e.g. 0,1,1,2,3,5,8,13,21,34,55,89,....etc. 
#
# Code should accept a single parameter to set the amount of numbers in the
# sequence to calculate, e.g. first 10 numbers, first 100, etc
# Format of output should be simply a list of numbers separated by a comma
# between each number; e.g. 0,1,1,2,3,5,8 etc..
# Interesting Variations score more points of course 
# Sequence always starts at 0,1 - so minimum sequence length is 2.

import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 1:
        print "Usage: python fibonacci.py num".format(len(argv[1:]))
        exit(-1)
    num = int(argv[1])
    

if __name__ == "__main__":
    sys.exit(main())
