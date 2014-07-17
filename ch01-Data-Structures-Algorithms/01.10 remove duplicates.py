# for hashable types (string, int, tuple)
def dedupe(items):
    seen = set() # prepare a set to hold values already passed
    for item in items:
        if item not in seen:
            yield item # return the item if it wasn't already passed
            seen.add(item) # add the item to the already passed set

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# for unhashable types (lists, dictionaries)
def dedupe(items, key=None):
    seen = set() # prepare a set to hold values already passed
    for item in items:
        # find the value based on the key
        val = item if key is None else key(item) 
        if val not in seen:
            yield item # return the item if the value it wasn't already passed
            seen.add(val) # add the value to the already passed set

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# set the key to be a tuple of the x and y values
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
# set the key to be an integer the x value
print(list(dedupe(a, key=lambda d: d['x'])))


# to eliminate duplicate lines in a file
with open('a.txt','r') as f:
    for line in dedupe(f):
        print(line)
