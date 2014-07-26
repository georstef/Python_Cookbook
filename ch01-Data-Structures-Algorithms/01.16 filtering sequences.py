mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# list comprehension
l = [n for n in mylist if n > 0]
print(l)

# list comprehension
l = [n for n in mylist if n < 0]
print(l)

# generator expression
pos = (n for n in mylist if n > 0) # with parenthesis not brackets
print(pos)
print(*pos, sep=', ') # cool trick for printing sequences
    

# using built in filter() function
l = ['1', '2', '-3', '-', '4', 'N/A', '5']

# the filtering code is a function that returns true or false
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

# filter() takes a callable that returns True-False and runs it for every item
#          and returns a filter object (which is an iterable object)
o = filter(is_int, l)
print(o)
ivals = list(o) # can be converted to list
print(ivals)

# itertools.compress(), takes an iterable and an accompanying Boolean selector
# as output, it gives all of the items in the iterable where
# the corresponding element in the selector is True
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
    ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
filtered_list = list(compress(addresses, more5))
print(filtered_list)
