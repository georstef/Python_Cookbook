# regular dictionary (contains lists)
d = {} 
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(4)
print(d)

from collections import defaultdict

# defaultdict object (contains lists)
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(4)
print(d)

# defaultdict object (contains sets)
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
d['b'].add(4)
print(d)
