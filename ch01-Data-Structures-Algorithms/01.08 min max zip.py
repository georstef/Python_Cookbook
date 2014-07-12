# regular dictionary
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
    }

# creates an iterator that can only be consumed once
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
# print(min(prices_and_names)) # this will return ValueError

# sorted will sort based on the keys of the dictionary
names_sorted = sorted(prices)
print(names_sorted) # just the names (sorted)

# sorted will sort based on the first value of the iterator then the second etc.
names_sorted = sorted(zip(prices.keys(), prices.values()))
print(names_sorted) # names and values

# min will find the minimun of the first value of the iterator then the second etc.
# (that's why we invert values and keys)
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

# max will find the maximum of the first value of the iterator then the second etc.
# (that's why we invert values and keys)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# sorted will sort based on the first value of the iterator then the second etc.
# (that's why we invert values and keys)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

