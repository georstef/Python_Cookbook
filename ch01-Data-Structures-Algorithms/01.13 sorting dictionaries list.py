rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

from operator import itemgetter

import pprint
pp = pprint.PrettyPrinter(indent=2)

# sort by first name
rows_by_fname = sorted(rows, key=itemgetter('fname'))
# print(rows_by_fname)
pp.pprint(rows_by_fname)
print('')

# sort by id
rows_by_uid = sorted(rows, key=itemgetter('uid'))
pp.pprint(rows_by_uid)
print('')

# sort first by last name and then with first name
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname')) # this is faster
# it's the same like -> sorted(rows, key=lambda r: (r['lname'], r['fname']))
pp.pprint(rows_by_lfname)


# another kind of dictionary sort
# sort first by values descending and then by key ascending
d = {"P1":77, "P2":89, "P3":77}
s = sorted(d.items(), key = lambda x:(-x[1], x[0]))
print(s) # ('P2', 89), ('P1', 77), ('P3', 77)]
