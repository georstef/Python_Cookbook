rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

from operator import itemgetter
from itertools import groupby

# sort by the desired field first
rows.sort(key=itemgetter('date'))

# iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

'''
GROUPBY()
The groupby() function works by scanning a sequence and finding sequential
“runs” of identical values (or values returned by the given key function).
On each iteration, it returns the value along with an iterator that produces
all of the items in a group with the same value.

An important preliminary step is sorting the data according to the field
of interest. Since groupby() only examines consecutive items,
failing to sort first won’t group the records as you want.
'''

'''
DEFAULTDICT
If the goal is to simply group the data together by dates into a large data
structure that allows random access, use defaultdict() to build a multidict
'''
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
# This allows the records for each date to be accessed easily like this:
for r in rows_by_date['07/01/2012']: # for specific date
    print(r)
