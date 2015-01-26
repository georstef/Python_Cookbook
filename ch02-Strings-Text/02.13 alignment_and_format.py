s = 'Hello World!'
print(s.ljust(20)) # prints 'Hello World!        '
print(s.rjust(20)) # prints '        Hello World!'
print(s.center(20)) # prints '    Hello World!    '

print('')

print(s.ljust(20, '*')) # prints 'Hello World!********'
print(s.rjust(20, '-')) # prints '--------Hello World!'
print(s.center(20, '=')) # prints '====Hello World!===='

print('')

print(format(s, '<20')) # prints 'Hello World!        '
print(format(s, '>20')) # prints '        Hello World!'
print(format(s, '^20')) # prints '    Hello World!    '

print('')

print(format(s, '*<20')) # prints 'Hello World!********'
print(format(s, '->20')) # prints '--------Hello World!'
print(format(s, '=^20')) # prints '====Hello World!===='

print('')

print('{:>10s} {:>10s}'.format('Hello', 'World')) # prints '     Hello      World'
print(format(1.2345, '>10')) # prints '    1.2345'
print(format(1.2345, '^10.2f')) # prints '   1.23   '
