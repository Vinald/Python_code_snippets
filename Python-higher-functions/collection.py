# collection: namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict, UserList, UserString

from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict, UserDict, UserList, UserString

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)
print()

#  counter
cnt = Counter([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
print(f'counter {cnt}')
print()
print(list(cnt.elements()))
print()

# orderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(f'order dict{od}')
print()

# defaultdict
dd = defaultdict(int)
dd['a'] = 1
dd['b'] = 2
print(dd['c'])
print()

# deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)
print()

# chainmap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain = ChainMap(dict1, dict2)
print(chain)
print()

# userdict
user = UserDict({'a': 1, 'b': 2})
print(user)
print()

# userlist  
user = UserList([1, 2, 3, 4, 5])
print(user)
print()

# userstring
user = UserString('python')
print(user)
print()
