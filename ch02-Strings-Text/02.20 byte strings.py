# indexing of byte strings produces integers,
a = 'Hello World' # Text string
print(a[0])  # H
print(a[1])  # e

b = b'Hello World' # Text string
print(b[0])  # 72
print(b[1])  # 101


# byte strings don’t provide a nice string representation
# and don’t print cleanly unless first decoded into a text string
print(b)
print(b.decode('ascii'))

# there are no string formatting operations available to byte strings
print('%10s %10d %10.2f' % ('ACME', 100, 490.1)) # this works
try:
    print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)) # this does not work
except:
    print('byte string error #1')

try:
    print(b'{} {} {}'.format(b'ACME', 100, 490.1)) # this does not work
except:
    print('byte string error #2')

# format as string and then encode to byte string
print('{} {} {}'.format('ACME', 100, 490.1).encode('ascii'))
    
    
