#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=1724

# Given a grid co-ordinate (x,y) as the centre point of a regular pentagon, 
# and the sum of the length of the sides, return the co-ordinates of each 
# point as: "Top", "MidLeft", "MidRight", "BottomLeft", "BottomRight" and 
# the distance from the centre to each of the points.
# 
# This should work for any possible position of the centre point, and any 
# length of the sides.
# 
# All Sides are equal length in a Regular Pentagon
# x = horizontal scale, y=vertical
# scale increments can be anything you wish.. mm, cm, inches, feet, etc 
# (doesn't matter) - though only whole units can be used
# 
# For added points, make it work for any regular polygon (and even further
# added points for calculating the area)

import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 4:
        print "Usage: python regular_polygon.py center-x center-y num-side total-circumference".format(len(argv[1:]))
        exit(-1)
    center = [ int(argv[1]), int(argv[2]) ]
    numSides = int(argv[3])
    totalCircum = int(argv[4])
    
    points = [];
    print points;

if __name__ == "__main__":
    sys.exit(main())


