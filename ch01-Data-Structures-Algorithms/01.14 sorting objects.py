class User:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return 'user{0}'.format(self.id)

import pprint
pp = pprint.PrettyPrinter(indent=2)

l=[User(10), User(3), User(5)]
pp.pprint(l)

# sort by id
lsorted = sorted(l, key=lambda o: o.id)
pp.pprint(lsorted)

from operator import attrgetter

# lambda o: o.id ======== attrgetter('id')
lreversesorted = sorted(l, key=attrgetter('id'), reverse=True)
pp.pprint(lreversesorted)


# attrgetter() can be applied to functions such as min() and max()
