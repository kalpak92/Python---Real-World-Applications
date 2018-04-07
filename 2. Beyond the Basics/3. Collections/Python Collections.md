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

Usually, a Python dictionary throws a `KeyError` if you try to get an item with a key that is not currently in the dictionary. The `defaultdict` in contrast will simply create any items that you try to access (provided of course they do not exist yet). To create such a "default" item, it calls the function object that you pass in the constructor (more precisely, it's an arbitrary "callable" object, which includes function and type objects). 

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

Using defaultdict

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

