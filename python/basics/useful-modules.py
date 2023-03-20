from collections import Counter, defaultdict, OrderedDict

# Counter: counts numbers of occurrences in an object
li = [1, 2, 3, 4, 5]
sentence = 'blah blah thinking about python'

print(Counter(li))
print(Counter(sentence))

# defaultdict
simple_dict = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
print(simple_dict['c'])

# OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

# datetime
import datetime

print(datetime.time(5, 45, 2))
print(datetime.date.today())

# arrays are more performant than lists
from array import array

arr = array('i', [1, 2, 3])
print(arr[1])
