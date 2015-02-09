n = 1234.56789
print(format(n, '0.2f'))
print(format(n, '>10.1f'))  # right align
print(format(n, '<10.1f'))  # left align
print(format(n, '^10.1f'))  # center align
print(format(n, '^10,.1f'))  # center align with thousands separator

swap_separators = { ord('.'):',', ord(','):'.' }
print(format(n, ',').translate(swap_separators))  # replaces all
print(format(n, ',').replace(',','.'))  # replaces only one

print('The value is {:0,.2f}'.format(n))  # string format
