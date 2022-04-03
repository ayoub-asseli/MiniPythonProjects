"""
In this challenge, sort a list containing a series of dates given as strings. Each date is given in the format DD-MM-YYYY_HH:MM:
"12-02-2012_13:44"

if mode is equal to "ASC", the list lst sorted in ascending order.
if mode is equal to "DSC", the list lst sorted in descending order.

Examples

sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ ["10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"]

sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ ["10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"]

sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ ["01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"]

"""

import time

def sort_dates(lst, mode):
    if mode == 'ASC':
        return sorted(lst, key= lambda date: time.strptime(date, "%d-%m-%Y_%H:%M"))
    else:
        return sorted(lst, key= lambda date: time.strptime(date, "%d-%m-%Y_%H:%M"))[::-1]
