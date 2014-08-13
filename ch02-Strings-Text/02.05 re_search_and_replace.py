text = 'yeah, sure can do, yeah!!!'

# simple replace
print("text->", text.replace('yeah', 'yep'))

print('----------------------------')

# for complicated matching use the re module
import re

text = 'Today is 13/08/2014 the wedding is 20/09/2014.'

# sub(match-pattern, replacement_pattern, text) function
print(text)
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', text))

print('----------------------------')

# same as above but with a compiled pattern 
datepattern = re.compile(r'(\d+)/(\d+)/(\d+)')  # creates a pattern object
print(datepattern.sub(r'\3-\2-\1', text))  # \3 means group number 3 etc..

print('----------------------------')

# for more complicated replacements use a callback function
from calendar import month_abbr
# the m here is a sre_match_object
def change_date(m):
    mon_name = month_abbr[int(m.group(2))]
    return '{} {} {}'.format(m.group(1), mon_name, m.group(3))
print(datepattern.sub(change_date, text))  


print('----------------------------')

# subn() for knowing how many replacements were made
newtext, n = datepattern.subn(r'\3-\1-\2', text)
print(newtext)
print('substitutions->', n)
