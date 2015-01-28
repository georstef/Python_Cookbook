parts = ['To', 'Be', 'Or', 'Not', 'To', 'Be']
print(' '.join(parts))
print('.'.join(parts))

# do NOT use this (sloooow)
s = ''
for p in parts:
    s += p
print(s)

# conversion with generator expression
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))


'''
I/O operations

# Version 1 (string concatenation)
f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
f.write(chunk1)
f.write(chunk2)

If the two strings are small, the first version might offer
much better performance due to the inherent expense of carrying out
an I/O system call.

On the other hand, if the two strings are large, the second version
may be more efficient, since it avoids making a large temporary result
and copying large blocks of memory around.

Again, it must be stressed that this is something you would have to study
in relation to your own data in order to determine which performs best.
'''
