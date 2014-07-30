line = 'asdf fjdk; afed, fjek,asdf, foo'
print(line)

#simple split
print(line.split())

# re.split
import re
# separator can be comma (,) or semicolon (;) or whitespace (\s)
print(re.split(r'[;,\s]\s*', line))


# keep the separators/delimeters (use parenthesis)
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2] # take one skip one
delimiters = fields[1::2] + [''] # take one skip one

# Reform 'line' string using the same delimiters
s = ''.join(v+d for v,d in zip(values, delimiters))
print(s)

# don't keep the separators/delimeters (use parenthesis with ?:)
s=re.split(r'(?:,|;|\s)\s*', line)
print(s)
