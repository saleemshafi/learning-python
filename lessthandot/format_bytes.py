#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=2245

# Given a numerical input of bytes, create a function to format the output
# to two decimal places along with the relevant postfixes
# Kilobytes
# Megabytes
# Gigabytes
# Terabytes
# Petabytes
# Exabytes
# Zettabytes
# Yottabytes


import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 1:
        print "Usage: python format_bytes.py bytes".format(len(argv[1:]))
        exit(-1)
    bytes = int(argv[1])

if __name__ == "__main__":
    sys.exit(main())
