#!/usr/bin/python

# http://forum.lessthandot.com/viewtopic.php?f=102&t=1608

# With another friday the thirteenth fast approaching, now seems like a good time for a themed 
# programming puzzle. The goal is to identify all friday the thirteenths for a given timeframe.
# We'll use a relatively small number of years, like 10. This should make it a little easier 
# in procedural languages.

import sys
from datetime import datetime

DATEFORMT = "%Y-%m-%d"


def thirteenths_between(start, end):
    while start <= end:
        yield start
        month = int(start.strftime("%m"))
        year = int(start.strftime("%Y"))
        if month == 12:
            start = start.replace(month=1, year=year+1)
        else:
            start = start.replace(month=month+1)

def count_fridays(thirteenths):
    return len(filter(lambda date: date.isoweekday() == 5, thirteenths))

def count_friday_thirteenths(start, end):
    count = 0
    while start <= end:
        if start.strftime("%w") == "5":
            count = count+1
        month = int(start.strftime("%m"))
        year = int(start.strftime("%Y"))
        if month == 12:
            start = start.replace(month=1, year=year+1)
        else:
            start = start.replace(month=month+1)
    return count

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv[1:]) != 2:
        print "need two date params, but got {0}".format(len(argv[1:]))
        exit(-1)
    dateFormat = "%Y-%m-%d"
    start = datetime.strptime(argv[1], dateFormat).date().replace(day=13)
    end = datetime.strptime(argv[2], dateFormat).date().replace(day=13)
    
    # count = count_friday_thirteenths(start, end)
    count = count_fridays( thirteenths_between(start, end));
    
    print "{2} Friday the 13ths between {0} and {1}".format(argv[1], argv[2], count) 

if __name__ == "__main__":
    sys.exit(main())

