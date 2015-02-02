s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(s)
print('----- 70 ------')
print(textwrap.fill(s, 70))
print('----- 40 ------')
print(textwrap.fill(s, 40))
print('----- 40+indent ------')
print(textwrap.fill(s, 40, initial_indent='   '))
print('----- 40+indent ------')
print(textwrap.fill(s, 40, subsequent_indent='   '))
