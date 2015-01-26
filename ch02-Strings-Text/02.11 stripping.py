s = '  hello   world---'
print(s)
print(s.strip())     # strips spaces and \n
print(s.lstrip())    # left strips spaces and \n
print(s.rstrip('-')) # right strips '-'
print(s.strip(' -')) # strips both space ' ' and '-'


s = '  hello   world   \n'
print(s)
import re
print(re.sub('\s+', ' ', s)) # multiple spaces are replaced by one space
print(re.sub('\s+', ' ', s.strip()))
