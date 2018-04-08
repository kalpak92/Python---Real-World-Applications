from collections import namedtuple

man = ('Ali', 30)
print(man[0])

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='perry', age=31, type='cat')
print(perry)
print(perry.name)
print(perry.__repr__())		#'Return a nicely formatted representation string'

print(perry._asdict())		#'Return a new OrderedDict which maps field names to their values'