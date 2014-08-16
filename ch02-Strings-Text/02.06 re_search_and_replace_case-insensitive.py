text = 'UPPER-CASE PYTHON, lower-case python, Camel-Case Python'

import re

# simple search
print("simple search->", re.findall('python', text))

print('----------------------------')

# case-insensitive search
print("case-insensitive search->", re.findall('python', text, flags=re.IGNORECASE))


print('----------------------------')

# case-insensitive replace
print("case-insensitive replace->", re.sub('python', 'snake', text, flags=re.IGNORECASE))

print('----------------------------')

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

# matchcase replace (matchcase.replace inner function is called for every match)
print("matchcase replace->", re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
