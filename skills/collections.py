from collections import *

a = ["aaabbbbbccccccccccccccd"]
my_counter = Counter(a)

point = namedtuple('point','x,y')
pt = point(1,2)

ordered_dict = OrderedDict()
ordered_dict['g'] = 2
ordered_dict['a'] = 1
print(ordered_dict)

d = defaultdict(float)
d['z'] = 1
d['b'] = 'hello'
print(d['c'])

a = deque()
a.append(1)
a.append(2)
a.appendleft(3)
print(a)
a.rotate()
print(a)
a.rotate()
print(a)
a.rotate()
print(a)

first = {'test':1, 'test2':2}
second = {'untested':-1,'untested2':-1}
print(ChainMap(first,second).maps)