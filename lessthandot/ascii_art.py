#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=1821

# This weeks challenge is to create some ASCII art in the shortest code possible. The 
# objectives are:
# * Be able to draw a solid circle/ellipse of user definable height and width and...
# * Be able to draw a solid triangle of user definable height and width
# * User should be able to choose at runtime to print either shape, or both
# * User should be able to choose the ASCII print character (which should be
#      consistent throughout the shapes.
# * Height and Width defined in characters (e.g. 3char x 3char)
# 
# Remember that the challenge here is to do this in the shortest code possible, so have
# fun streamlining, optimising and essentially making it unreadable but very short.

import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 4:
        print "Usage: python ascii_art.py [circle|triangle] fill-character height width".format(len(argv[1:]))
        exit(-1)
    shape = int(argv[1])
    fill = argv[2]
    height = int(argv[3])
    width = int(argv[4])
    

if __name__ == "__main__":
    sys.exit(main())


