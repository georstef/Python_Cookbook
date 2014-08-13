text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print("text == 'yeah'->", text == 'yeah')

# Match at start
print("startswith('yeah')->", text.startswith('yeah'))  # false

# Match at end
print("endswith('no')->", text.endswith('no'))   # true

# Search for the location of the first occurrence
print("find('no')->", text.find('no'))  # false

print('----------------------------')

# for complicated matching use the re module
import re

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
text3 = '111/271/20121abc'

# Simple matching: \d+ means match one or more (d)igits
# match() always tries to find the match at the start of a string
# returns an object with only the part of the string that matches
print(re.match(r'\d+/\d+/\d+', text1)) # SRE_Match object
print(re.match(r'\d+/\d+/\d+', text2)) # None
print(re.match(r'\d+/\d+/\d+', text3)) # SRE_Match object

print('----------------------------')

# same as above but with a compiled pattern 
datepattern = re.compile(r'\d+/\d+/\d+')  # creates a pattern object
print(datepattern.match(text1)) # SRE_Match object
print(datepattern.match(text2)) # None
print(datepattern.match(text3)) # SRE_Match object

print('----------------------------')

# findall() searches text for all occurrences of a pattern
text = 'Today is 13/08/2014 the wedding is 20/09/2014.'
print(datepattern.findall(text)) # returns a list of strings

print('----------------------------')

# parenthesis in patterns creates groups
datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepattern.match(text1)
print(m)           # SRE_Match object
print(m.group(0))  # 11/27/2012
print(m.group(1))  # 11
print(m.group(2))  # 27
print(m.group(3))  # 2012
# print(m.group(4))  # index error
print(m.groups())  # ('11', '27', '2012')
month, day, year = m.groups() # unpacks the group tuple

print('----------------------------')

# findall() in groups
print(datepattern.findall(text))
for day, month, year in datepattern.findall(text):
    print('{}-{}-{}'.format(year, month, day))

print('----------------------------')

# finditer() returns what findall() returns but one at a time
for m in datepattern.finditer(text):
    print(m.groups())
