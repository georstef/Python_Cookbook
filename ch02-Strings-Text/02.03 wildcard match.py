from fnmatch import fnmatch, fnmatchcase

print(fnmatch('Dat45.csv', 'Dat*')) # true
print(fnmatch('Dat45.csv', 'Dat[0-9]*')) # true
print(fnmatch('Dat45.csv', 'Dat[0-9][0-9]*')) # true

print(fnmatch('Dat1a.csv', 'Dat[0-9][0-9]*')) # false

# fnmatch -> not case sensitive in windows (depends on OS)
print(fnmatch('foo.txt', '*.TXT')) # true
# fnmatchcase -> case sensitive
print(fnmatchcase('foo.txt', '*.TXT')) # false

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
    ]
a = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
print(*a, sep='|')
b = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
print(*b, sep='|')

