# regular dictionary
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
    }

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
    }

# Find keys in common
print(a.keys() & b.keys()) # -> { 'x', 'y' }

# Find keys in A that are not in B
print(a.keys() - b.keys()) # -> { 'z' }

# Find (key,value) pairs in common
print(a.items() & b.items()) # -> { ('y', 2) }

# Make a new key list with certain keys removed
c = [key for key in a.keys() - {'z', 'w'}]
print(c) # -> {'x': 1, 'y': 2}

# Make a new dictionary with certain keys removed
# key => the key of the new dict
# a[key] for key in a.keys() - {'z', 'w'} => the value of the new dict
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c) # -> {'x': 1, 'y': 2}

