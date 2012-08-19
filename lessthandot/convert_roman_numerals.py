#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=2361

# Write a program to convert to (and from) roman numerals. So your program should be
# able to take the input of 27 and return XXVII, and take MCMLXXXI and return 1981.
# And of course any other values. 

# The program must work for all numbers between the upper bound of 4000 and the lower
# bound of 0 (both non-inclusive) 

# Bonus points if you check incoming roman numerals for well-formedness (this lists
# some of the rules: http://en.wikipedia.org/wiki/Roman_nume ... n_numerals)


import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 1:
        print "Usage: python convert_roman_numerals.py number".format(len(argv[1:]))
        exit(-1)
    number = int(argv[1])
    

if __name__ == "__main__":
    sys.exit(main())
