s1 = 'Spicy Jalape\u00f1o' # composed “ñ” character (U+00F1)
s2 = 'Spicy Jalapen\u0303o' # Latin letter “n” followed by a “~” combining character (U+0303)
print(s1)
print(s2)
print('s1==s2 => ', s1==s2)
print('len(s1) => ', len(s1))
print('len(s2) => ', len(s2))

print('-------------')

import unicodedata
n1 = unicodedata.normalize('NFC', s1) # NFC means that characters should be fully composed
n2 = unicodedata.normalize('NFC', s2) # N-Normalize F-Fully C-Composed
print('normalized s1 => ', ascii(n1))
print('normalized s2 => ', ascii(n2))
print('normalized s1==s2 => ', n1==n2)

print('-------------')

n3 = unicodedata.normalize('NFD', s1) # NFD means that characters should be fully decomposed
n4 = unicodedata.normalize('NFD', s2) # N-Normalize F-Fully D-Decomposed
print('normalized s1 => ', ascii(n3))
print('normalized s2 => ', ascii(n4))
print('normalized s1==s2 => ', n3==n4)

print('-------------')

# unicodedata.combining-> checks if a specific character is a combining character
print('normalized s1 => ', ascii(n3))
n5 = ''.join(c for c in n3 if not unicodedata.combining(c)) 
print(n5)
