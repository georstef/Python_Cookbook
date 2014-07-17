######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'

# get the numbers from a string based on position
cost = int(record[20:32]) * float(record[40:48])
print(cost)

# using the build in slice() function
QUANTITY = slice(20,32) # equals to 20:32
PRICE = slice(40,48)  # equals to 40:48
cost = int(record[QUANTITY]) * float(record[PRICE])
print(cost)

# slice() returns a slice object with attributes (start, stop, step)
print(QUANTITY.start)
print(QUANTITY.stop)
print(QUANTITY.step)

# also has the indices() method (needs revisit)
