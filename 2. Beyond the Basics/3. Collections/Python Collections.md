# Python: Collections

Python ships with a module that contains a number of container data types called Collections. 

The ones which we will talk about are:

- `defaultdict`
- `OrderedDict`
- `counter`
- `deque`
- `namedtuple`
- `enum.Enum` (outside of the module; Python 3.4+)

This module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers, [`dict`](https://docs.python.org/2/library/stdtypes.html#dict), `list`, [`set`](https://docs.python.org/2/library/stdtypes.html#set), and [`tuple`](https://docs.python.org/2/library/functions.html#tuple).

| [`namedtuple()`](https://docs.python.org/2/library/collections.html#collections.namedtuple) | factory function for creating tuple subclasses with named fields | New in version 2.6. |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------- |
| [`deque`](https://docs.python.org/2/library/collections.html#collections.deque) | list-like container with fast appends and pops on either end | New in version 2.4. |
| [`Counter`](https://docs.python.org/2/library/collections.html#collections.Counter) | dict subclass for counting hashable objects                  | New in version 2.7. |
| [`OrderedDict`](https://docs.python.org/2/library/collections.html#collections.OrderedDict) | dict subclass that remembers the order entries were added    | New in version 2.7. |
| [`defaultdict`](https://docs.python.org/2/library/collections.html#collections.defaultdict) | dict subclass that calls a factory function to supply missing values | New in version 2.5. |

## **1. `defaultdict`**

**Unlike `dict`, with `defaultdict` you do not need to check whether a key is present or not. **

Usually, a Python dictionary throws a `KeyError` if you try to get an item with a key that is not currently in the dictionary. 

The `defaultdict` in contrast will simply create any items that you try to access (provided of course they do not exist yet). To create such a "default" item, it calls the function object that you pass in the constructor (more precisely, it's an arbitrary "callable" object, which includes function and type objects). 

```python
users = {'bob': 'coder'}
print(users['bob'])
print(users['julian'])  # oops
```

```python
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-10-2d801425e069> in <module>()
      1 users['bob']
----> 2 users['julian']  # oops

KeyError: 'julian'
```

You can get around it with dict's get method:

```python
print (users.get('bob'))
```

Output: `coder`

```python
print(users.get('julian') is None)
```

Output: `True`

But what if you need to build up a collection though? Let's make a dict from the following list of tuples:

```python
challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(challenges_done)
```

Output:

```python
[('mike', 10),
 ('julian', 7),
 ('bob', 5),
 ('mike', 11),
 ('julian', 8),
 ('bob', 6)]
```

```python
challenges = {}
for name, challenge in challenges_done:
    challenges[name].append(challenge)
```

```python
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-14-5d8074648e43> in <module>()
      1 challenges = {}
      2 for name, challenge in challenges_done:
----> 3     challenges[name].append(challenge)

KeyError: 'mike'
```

**Using defaultdict**

```python
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)
```

```python
defaultdict(list, {'bob': [5, 6], 'julian': [7, 8], 'mike': [10, 11]})
```

### `defaultdict` example

```python
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

# output
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })
```

Using `list` as the `default_factory`, it is easy to group a sequence of key-value pairs into a dictionary of lists:

```python
>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

When each key is encountered for the first time, it is not already in the mapping; so an entry is automatically created using the `default_factory` function which returns an empty `list`. The `list.append()` operation then attaches the value to the new list. When keys are encountered again, the look-up proceeds normally (returning the list for that key) and the `list.append()` operation adds another value to the list. This technique is simpler and faster than an equivalent technique using [`dict.setdefault()`](https://docs.python.org/2/library/stdtypes.html#dict.setdefault):

```python
>>> d = {}
>>> for k, v in s:
...     d.setdefault(k, []).append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

Setting the `default_factory` to [`int`](https://docs.python.org/2/library/functions.html#int) makes the [`defaultdict`](https://docs.python.org/2/library/collections.html#collections.defaultdict) useful for counting (like a bag or multiset in other languages):

```python
>>> s = 'mississippi'
>>> d = defaultdict(int)
>>> for k in s:
...     d[k] += 1
...
>>> d.items()
[('i', 4), ('p', 2), ('s', 4), ('m', 1)]
```

When a letter is first encountered, it is missing from the mapping, so the `default_factory` function calls [`int()`](https://docs.python.org/2/library/functions.html#int) to supply a default count of zero. The increment operation then builds up the count for each letter.

Setting the `default_factory` to [`set`](https://docs.python.org/2/library/stdtypes.html#set) makes the [`defaultdict`](https://docs.python.org/2/library/collections.html#collections.defaultdict) useful for building a dictionary of sets:

```python
>>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
>>> d = defaultdict(set)
>>> for k, v in s:
...     d[k].add(v)
...
>>> d.items()
[('blue', set([2, 4])), ('red', set([1, 3]))]
```



## 2. `OrderedDict`

`OrderedDict` keeps its entries sorted as they are initially inserted. Overwriting a value of an existing key doesn’t change the position of that key. However, deleting and reinserting an entry moves the key to the end of the dictionary.

**Problem:**

```python
colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key, value)
# Output:
#   Green 170
#   Blue 160
#   Red 198
# Entries are retrieved in an unpredictable order
```

**Solution:**

```python
from collections import OrderedDict

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)
# Output:
#   Red 198
#   Green 170
#   Blue 160
# Insertion order is preserved
```

`OrderedDict.``popitem`(*last=True*)

The [`popitem()`](https://docs.python.org/2/library/collections.html#collections.OrderedDict.popitem) method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if *last* is true or FIFO order if false.

In addition to the usual mapping methods, ordered dictionaries also support reverse iteration using [`reversed()`](https://docs.python.org/2/library/functions.html#reversed).

Equality tests between [`OrderedDict`](https://docs.python.org/2/library/collections.html#collections.OrderedDict) objects are order-sensitive and are implemented as `list(od1.items())==list(od2.items())`. Equality tests between [`OrderedDict`](https://docs.python.org/2/library/collections.html#collections.OrderedDict)objects and other [`Mapping`](https://docs.python.org/2/library/collections.html#collections.Mapping) objects are order-insensitive like regular dictionaries. This allows [`OrderedDict`](https://docs.python.org/2/library/collections.html#collections.OrderedDict) objects to be substituted anywhere a regular dictionary is used.

## 3. `counter`

A [`Counter`](https://docs.python.org/2/library/collections.html#collections.Counter) is a [`dict`](https://docs.python.org/2/library/stdtypes.html#dict) subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The [`Counter`](https://docs.python.org/2/library/collections.html#collections.Counter) class is similar to bags or multisets in other languages.

Elements are counted from an *iterable* or initialized from another *mapping* (or counter):

```python
c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args
```

Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a [`KeyError`](https://docs.python.org/2/library/exceptions.html#exceptions.KeyError):

```python
c = Counter(['eggs', 'ham'])
c['bacon']                              # count of a missing element is zero
0
```

Setting a count to zero does not remove an element from a counter. Use `del` to remove it entirely:

```python
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry
```

### Common patterns for working with [`Counter`](https://docs.python.org/2/library/collections.html#collections.Counter) objects

```python
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
```

### Examples

Counter allows us to count the occurrences of a particular item. For instance it can be used to count the number of individual favourite colours:

```python
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)
# Output: Counter({
#    'Yasoob': 2,
#    'Ali': 2,
#    'Arham': 1,
#    'Ahmed': 1
# })
```

We can also count the most common lines in a file using it. For example:

```python
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
```

One of my favorites. Say you want to count the most common words in a text:

```python
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()

print(words[:5])
['Lorem', 'Ipsum', 'is', 'simply', 'dummy']
```

Before getting to know `collections` I would has written something like this:

```python
common_words = {}

for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k ,v)
```

Output:

```
the 6
Lorem 4
Ipsum 4
of 4
and 3
```

Now compare this to using `Counter` and its `most_common` method:

```
Counter(words).most_common(5)
```

Output:

```python
[('the', 6), ('Lorem', 4), ('Ipsum', 4), ('of', 4), ('and', 3)]
```

#### Mathematical Operations

Several mathematical operations are provided for combining [`Counter`](https://docs.python.org/2/library/collections.html#collections.Counter) objects to produce multisets (counters that have counts greater than zero). Addition and subtraction combine counters by adding or subtracting the counts of corresponding elements. Intersection and union return the minimum and maximum of corresponding counts. Each operation can accept inputs with signed counts, but the output will exclude results with counts of zero or less.

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
```



## 4. `deque`

`deque` provides you with a double ended queue which means that you can append and delete elements from either side of the queue. 

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

First of all you have to import the deque module from the collections library:

```python
from collections import deque
```

Now we can instantiate a deque object.

```
d = deque()
```

It works like python lists and provides you with somewhat similar methods as well. For example you can do:

```python
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'
```

You can pop values from both sides of the deque:

```python
d = deque(range(5))
print(len(d))
# Output: 5

d.popleft()
# Output: 0

d.pop()
# Output: 4

print(d)
# Output: deque([1, 2, 3])
```

We can also limit the amount of items a deque can hold. By doing this when we achieve the maximum limit of our deque it will simply pop out the items from the opposite end. It is better to explain it using an example so here you go:

```python
d = deque(maxlen=30)
```

Now whenever you insert values after 30, the leftmost value will be popped from the list. 

You can also expand the list in any direction with new values:

```python
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
# Output: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

Let's do some removing and inserting at random locations in the sequence, a `list` is slow at this because it needs to move all adjacent around ([Grokking Algorithms](https://pybit.es/grokking_algorithms.html) explains this really well). Here is where `deque` is a big win:

```python
def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

%timeit insert_and_delete(lst)
# Output:
# 447 ms ± 45.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%timeit insert_and_delete(deq)
# Output:
# 83.7 µs ± 13.7 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```



## 5. `namedtuple`

You might already be acquainted with tuples. A tuple is basically a immutable list which allows you to store a sequence of values separated by commas. They are just like lists but have a few key differences. The major one is that unlike lists, **you can not reassign an item in a tuple**. In order to access the value in a tuple you use integer indexes like:

```python
man = ('Ali', 30)
print(man[0])
# Output: Ali
```

Well, so now what are `namedtuples`? 

Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.

They turn tuples into convenient containers for simple tasks. With namedtuples you don’t have to use integer indexes for accessing members of a tuple. You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'
```

You can now see that we can access members of a tuple just by their name using a `.`. Let’s dissect it a little more. A named tuple has two required arguments. They are the tuple name and the tuple field_names. In the above example our tuple name was ‘Animal’ and the tuple field_names were ‘name’, ‘age’ and ‘type’. Namedtuple makes your tuples **self-document**. You can easily understand what is going on by having a quick glance at your code. And as you are not bound to use integer indexes to access members of a tuple, it makes it more easy to maintain your code. Moreover, as **`namedtuple` instances do not have per-instance dictionaries**, they are lightweight and require no more memory than regular tuples. This makes them faster than dictionaries. However, do remember that as with tuples, **attributes in namedtuples are immutable**. It means that this would not work:

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42

# Output: Traceback (most recent call last):
#            File "", line 1, in
#         AttributeError: can't set attribute
```

You should use named tuples to make your code self-documenting. **They are backwards compatible with normal tuples**. It means that you can use integer indexes with namedtuples as well:

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
# Output: perry
```

Last but not the least, you can convert a namedtuple to a dictionary. Like this:

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
# Output: OrderedDict([('name', 'Perry'), ('age', 31), ...
```