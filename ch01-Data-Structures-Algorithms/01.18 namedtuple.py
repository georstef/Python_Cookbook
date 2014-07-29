from collections import namedtuple

# create a class that takes 2 arguments (like a record)
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# Subscriber objects do everything a tuple can do
# eg. len() - unpacking - is immutable

# instantiate an object (of the named tupled class)
sub = Subscriber('test@example.com', '2012-10-19')

print(sub) # show the object

print(sub.addr) # show a field of the object/record
print(sub[0]) # it's the same as positional elements

print(sub.joined) # show another field of the object/record
print(sub[1]) # it's the same as positional elements

# since it is immutable the only way to replace a value is
sub = sub._replace(addr='info@example.com')
print(sub)
