#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=1938

# TAll we want you to do is find every prime number between 0 and 1,000,000. That's it.  
#
# A prime number is a number that can only be divided by itself and 1 to result in a whole
# number. E.g. 2, 3 and 5 are all prime, but 4 can be divided by 2 aswell as 4 and 1, so
# it is not.
#
# The faster your code is, the better - so if you were thinking of looping through each
# number, that may not be the most efficient route... 
#
# For extra points, find the Mersenne primes too.
#
# For even more extra points we challenge you to find all the primes between 0 and 10,000,000.
# And for those hardcore geeks - how about 0 to 2,147,483,647 (the maximum for a 32 bit
# integer).

import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 1:
        print "Usage: python prime_numbers.py max".format(len(argv[1:]))
        exit(-1)
    maxNum = int(argv[1])
    

if __name__ == "__main__":
    sys.exit(main())
