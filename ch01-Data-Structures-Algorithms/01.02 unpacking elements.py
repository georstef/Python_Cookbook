def drop_first_last(a_lot_of_stuff):
  first, *middle, last = a_lot_of_stuff
  return avg(middle)

# -----------------------------------------

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record

print(name)
print(email)
print(phone_numbers)

# -----------------------------------------

records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# -----------------------------------------

*trailing_qtrs, current_qtr = [10, 8, 7, 3]
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg, '-', current_qtr)
