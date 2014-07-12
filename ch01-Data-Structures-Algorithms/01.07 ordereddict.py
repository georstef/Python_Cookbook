# regular dictionary
d = {} 
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
print(d) # prints in no particular order

from collections import OrderedDict

# ordereddict object
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
print(d) # prints in order of insertion

# helpful for creating json with specific field order
import json
j = json.dumps(d)
print(j)
