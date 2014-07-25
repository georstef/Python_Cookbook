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
