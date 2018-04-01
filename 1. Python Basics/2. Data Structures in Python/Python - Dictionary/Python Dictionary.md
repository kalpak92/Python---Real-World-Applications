# Python Dictionary

Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.

Dictionaries are optimized to retrieve values when the key is known.

Python's efficient key/value hash table structure is called a "dict". The contents of a dict can be written as a series of key:value pairs within braces { }, e.g. dict = {key1:value1, key2:value2, ... }. The "empty dict" is just an empty pair of curly braces {}.

Looking up or setting a value in a dict uses square brackets, e.g. dict['foo'] looks up the value under the key 'foo'. **Strings, numbers, and tuples work as keys, and any type can be a value**. Other types may or may not work correctly as keys (strings and tuples work cleanly since they are immutable). Looking up a value which is not in the dict throws a KeyError -- use "in" to check if the key is in the dict, or use dict.get(key) which returns the value or None if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).

```python
## Can build up a dict by starting with the the empty dict {}
  ## and storing key/value pairs into the dict like this:
  ## dict[key] = value-for-that-key
  dict = {}
  dict['a'] = 'alpha'
  dict['g'] = 'gamma'
  dict['o'] = 'omega'

  print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

  print dict['a']     ## Simple lookup, returns 'alpha'
  dict['a'] = 6       ## Put new key/value into dict
  'a' in dict         ## True
  ## print dict['z']                  ## Throws KeyError
  if 'z' in dict: print dict['z']     ## Avoid KeyError
  print dict.get('z')  ## None (instead of KeyError)
```

## How to create a dictionary?

Creating a dictionary is as simple as placing items inside curly braces {} separated by comma.

An item has a key and the corresponding value expressed as a pair, key: value.

While values can be of any data type and can repeat, keys must be of immutable type ([string](https://www.programiz.com/python-programming/string), [number](https://www.programiz.com/python-programming/numbers) or [tuple](https://www.programiz.com/python-programming/tuple) with immutable elements) and must be unique.

```python
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```

As you can see above, we can also create a dictionary using the built-in function `dict()`.

## How to access elements from a dictionary?

While indexing is used with other container types to access values, dictionary uses keys. Key can be used either inside square brackets or with the `get()` method.

The difference while using `get()` is that it returns `None` instead of `KeyError`, if the key is not found.

```python
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']
```

When you run the program, the output will be:

```python
Jack
26
```

## How to change or add elements in a dictionary?

Dictionary are mutable. We can add new items or change the value of existing items using assignment operator.

If the key is already present, value gets updated, else a new key: value pair is added to the dictionary.

```python
my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)
```

When you run the program, the output will be:

```python
{'name': 'Jack', 'age': 27}
{'name': 'Jack', 'age': 27, 'address': 'Downtown'}
```

## How to delete or remove elements from a dictionary?

We can remove a particular item in a dictionary by using the method `pop()`. This method removes as item with the provided key and **returns the value**.

The method, `popitem()` can be used to remove and **return an arbitrary item** (key, value) form the dictionary. All the items can be removed at once using the `clear()` method.

We can also use the `del` keyword to remove individual items or the entire dictionary itself.

```python
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]  

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)
```

When you run the program, the output will be:

```python
16
{1: 1, 2: 4, 3: 9, 5: 25}
(1, 1)
{2: 4, 3: 9, 5: 25}
{2: 4, 3: 9}
{}
```

## Python Dictionary Methods

Methods that are available with dictionary are tabulated below. Some of them have already been used in the above examples.

| Method                                                       | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [clear()](https://www.programiz.com/python-programming/methods/dictionary/clear) | Remove all items form the dictionary.                        |
| [copy()](https://www.programiz.com/python-programming/methods/dictionary/copy) | Return a shallow copy of the dictionary.                     |
| [fromkeys(seq[, v\])](https://www.programiz.com/python-programming/methods/dictionary/fromkeys) | Return a new dictionary with keys from seq and value equal to v(defaults to `None`). |
| [get(key[,d\])](https://www.programiz.com/python-programming/methods/dictionary/get) | Return the value of key. If key doesnot exit, return d (defaults to `None`). |
| [items()](https://www.programiz.com/python-programming/methods/dictionary/items) | Return a new view of the dictionary's items (key, value).    |
| [keys()](https://www.programiz.com/python-programming/methods/dictionary/keys) | Return a new view of the dictionary's keys.                  |
| [pop(key[,d\])](https://www.programiz.com/python-programming/methods/dictionary/pop) | Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises `KeyError`. |
| [popitem()](https://www.programiz.com/python-programming/methods/dictionary/popitem) | Remove and return an arbitary item (key, value). Raises `KeyError` if the dictionary is empty. |
| [setdefault(key[,d\])](https://www.programiz.com/python-programming/methods/dictionary/setdefault) | If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to `None`). |
| [update([other\])](https://www.programiz.com/python-programming/methods/dictionary/update) | Update the dictionary with the key/value pairs from other, overwriting existing keys. |
| [values()](https://www.programiz.com/python-programming/methods/dictionary/values) | Return a new view of the dictionary's values                 |

Here are a few example use of these methods.

```python
marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))
```

## Python Dictionary Comprehension

Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.

Dictionary comprehension consists of an expression pair (key: value) followed by `for`statement inside curly braces {}.

Here is an example to make a dictionary with each item being a pair of a number and its square.

```python
squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
```

This code is equivalent to

```python
squares = {}
for x in range(6):
   squares[x] = x*x
```

A dictionary comprehension can optionally contain more [for](https://www.programiz.com/python-programming/for-loop) or [if statements](https://www.programiz.com/python-programming/if-elif-else).

An optional `if` statement can filter out items to form the new dictionary.

Here are some examples to make dictionary with only odd items.

```python
odd_squares = {x: x*x for x in range(11) if x%2 == 1}

# Output: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(odd_squares)
```

## Other Dictionary Operations

### Dictionary Membership Test

We can test if a key is in a dictionary or not using the keyword `in`. Notice that membership test is for keys only, not for values.

```python
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)

# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)
```

### Iterating Through a Dictionary

Using a `for` loop we can iterate though each key in a dictionary.

```python
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
```

### Dict Formatting

The % operator works conveniently to substitute values from a dict into a string by name:

```python
  hash = {}
  hash['word'] = 'garfield'
  hash['count'] = 42
  s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
  # 'I want 42 copies of garfield'
```

### Built-in Functions with Dictionary

Built-in functions like `all()`, `any()`, `len()`, `cmp()`, `sorted()` etc. are commonly used with dictionary to perform different tasks.

| Function                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [all()](https://www.programiz.com/python-programming/methods/built-in/all) | Return `True` if all keys of the dictionary are true (or if the dictionary is empty). |
| [any()](https://www.programiz.com/python-programming/methods/built-in/any) | Return `True` if any key of the dictionary is true. If the dictionary is empty, return `False.` |
| [len()](https://www.programiz.com/python-programming/methods/built-in/len) | Return the length (the number of items) in the dictionary.   |
| cmp()                                                        | Compares items of two dictionaries.                          |
| [sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | Return a new sorted list of keys in the dictionary.          |

Here are some examples that uses built-in functions to work with dictionary.

```python
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares))
```

