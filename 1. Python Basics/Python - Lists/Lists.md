# Python Lists

Python has a great built-in list type named "list". List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0. (See the official [python.org list docs](http://docs.python.org/tut/node7.html).)

```python
colors = ['red', 'blue', 'green']
  print colors[0]    ## red
  print colors[2]    ## green
  print len(colors)  ## 3
```

![list of strings 'red' 'blue 'green'](https://developers.google.com/edu/python/images/list1.png)

Assignment with an = on lists does not make a copy. Instead, assignment makes the two variables point to the one list in memory.

```python
b = colors   ## Does not copy the list
```

![both colors and b point to the one list](https://developers.google.com/edu/python/images/list2.png)

The "empty list" is just an empty pair of brackets [ ]. 

- The '+' works to append two lists, so [1, 2] + [3, 4] yields [1, 2, 3, 4] (this is just like + with strings).

## FOR and IN

Python's *for* and *in* constructs are extremely useful, and the first use of them we'll see is with lists. The *for* construct -- `for **var** in **list**` -- is an easy way to look at each element in a list (or other collection). Do not add or remove from the list during iteration.

```python
  squares = [1, 4, 9, 16]
  sum = 0
  for num in squares:
    sum += num
  print sum  ## 30
```

If you know what sort of thing is in the list, use a variable name in the loop that captures that information such as "num", or "name", or "url". Since python code does not have other syntax to remind you of types, your variable names are a key way for you to keep straight what is going on.

The *in* construct on its own is an easy way to test if an element appears in a list (or other collection) -- `**value** in**collection**` -- tests if the value is in the collection, returning True/False.

```python
  list = ['larry', 'curly', 'moe']
  if 'curly' in list:
    print 'yay'
```

The for/in constructs are very commonly used in Python code and work on data types other than list, so you should just memorize their syntax. You may have habits from other languages where you start manually iterating over a collection, where in Python you should just use for/in.

You can also use for/in to work on a string. The string acts like a list of its chars, so `for ch in s: print ch` prints all the chars in a string.

### Range

The range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1, ... b-1 -- up to but not including the last number. The combination of the for-loop and the range() function allow you to build a traditional numeric for loop:

```python
  ## print the numbers from 0 through 99
  for i in range(100):
    print i
```

There is a variant xrange() which avoids the cost of building the whole list for performance sensitive cases (in Python 3000, range() will have the good performance behavior and you can forget about xrange()).

#### Difference: xrange vs range 

- **range()** – This returns a list of numbers created using range() function.
- **xrange()** – This function returns the **generator object** that can be used to display numbers only by looping. Only particular range is displayed on demand and hence called “**lazy evaluation**“.

For the most part, `xrange` and `range` are the exact same in terms of functionality. They both provide a way to generate a list of integers for you to use, however you please. The only difference is that `range` returns a Python `list` object and `xrange` returns an `xrange` object.

What does that mean? It means that `xrange` doesn't actually generate a static list at run-time like `range` does. It creates the values as you need them with a special technique called *yielding*. This technique is used with a type of object known as *generators*.

- range() returns – the **list** as return type.
- xrange() returns – **xrange()** object.

Okay, now what does *that* mean?  *That* means that if you have a really gigantic range you'd like to generate a list for, say one billion, `xrange` is the function to use. This is especially true if you have a really memory sensitive system such as a cell phone that you are working with, as `range` will use as much memory as it can to create your array of integers, which can result in a `MemoryError` and crash your program. It's a memory hungry beast.

That being said, if you'd like to iterate over the list multiple times, it's probably better to use `range`. This is because `xrange` has to generate an integer object every time you access an index, whereas `range` is a static list and the integers are already "there" to use.

```python
# Python code to demonstrate range() vs xrange()
# on  basis of memory
 
import sys
 
# initializing a with range()
a = range(1,10000)
 
# initializing a with xrange()
x = xrange(1,10000)
 
# testing the size of a
# range() takes more memory
print ("The size allotted using range() is : ")
print (sys.getsizeof(a))
 
# testing the size of a
# range() takes less memory
print ("The size allotted using xrange() is : ")
print (sys.getsizeof(x))
```

Output:

```python
The size allotted using range() is : 
80064
The size allotted using xrange() is : 
40
```

The functions `xrange` and `range` take in three arguments in total, however two of them are optional. The arguments are "start", "stop" and "step". "start" is what integer you'd like to start your list with, "stop" is what integer you'd like your list to stop at, and "step" is what your list elements will increment by.

### While Loop

Python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and Java, altering the course of the innermost loop. The above for/in loops solves the common case of iterating over every element in a list, but the while loop gives you total control over the index numbers. Here's a while loop which accesses every 3rd element in a list:

```python
  ## Access every 3rd element in a list
  i = 0
  while i < len(a):
    print a[i]
    i = i + 3
```

## List Methods

Here are some other common list methods.

- list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
- list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
- list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
- list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
- list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
- list.sort() -- sorts the list **in place** (does not return it). (The sorted() function shown below is preferred.)
- list.reverse() -- reverses the list in place (does not return it)
- list.pop(index) -- removes and **returns the element at the given index**. Returns the rightmost element if index is omitted (roughly the opposite of append()).

Notice that these are ***methods* on a list object**, while **len() is a function that takes the list** (or string or whatever) as an argument.

```python
list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print list.index('curly')    ## 2

  list.remove('curly')         ## search and remove that element
  list.pop(1)                  ## removes and returns 'larry'
  print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
```

Common error: note that the above methods do not *return* the modified list, they just modify the original list.

```python
  list = [1, 2, 3]
  print list.append(4)   ## NO, does not work, append() returns None
  ## Correct pattern:
  list.append(4)
  print list  ## [1, 2, 3, 4]
```

### List Build Up

One common pattern is to start a list a the empty list [], then use append() or extend() to add elements to it:

```python
  list = []          ## Start as the empty list
  list.append('a')   ## Use append() to add elements
  list.append('b')
```

### List Slices

Slices work on lists just as with strings, and can also be used to change sub-parts of the list.

```python
  list = ['a', 'b', 'c', 'd']
  print list[1:-1]   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print list         ## ['z', 'c', 'd']
```

The ASCII art diagram is helpful too for remembering how slices work:

```
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

It's pretty simple really:

```python
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
```

There is also the `step` value, which can be used with any of the above:

```python
a[start:end:step] # start through not past end, by step
```

The key point to remember is that the `:end` value represents the first value that is *not* in the selected slice. So, the difference beween `end` and `start` is the number of elements selected (if `step` is 1, the default).

The other feature is that `start` or `end` may be a *negative* number, which means it counts from the end of the array instead of the beginning. So:

```python
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
a[::-1]  # reverse a string.
```

Here are some more examples of slicing lists if you're still not sure how slicing works.

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#Here is how to access the first three items (from first to third):
days[0:3]	#['Mon', 'Tue', 'Wed']

#Access items from first to fourth:
days[0:4] 	#['Mon', 'Tue', 'Wed', 'Thu']

#Exactly the same as above
days[:4] 	#['Mon', 'Tue', 'Wed', 'Thu'] 

#No boundaries
days[:] 	#['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] 

#From first to second-to-last
days[0:-1] 	#['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

#From first to third-to-last
days[:-2]	#['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

#From third-to-last to second-to-last
days[-3:-1] #['Fri', 'Sat'] 

#From third-to-last to last
days[-3:] 	#['Fri', 'Sat', 'Sun']

```

### How to change or add elements to a list?

List are mutable, meaning, their elements can be changed unlike [string](https://www.programiz.com/python-programming/string) or [tuple](https://www.programiz.com/python-programming/tuple).

We can use assignment operator (=) to change an item or a range of items.

```python
# mistake values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

# Output: [1, 3, 5, 7]
print(odd)      
```

We can add one item to a list using `append()` method or add several items using `extend()`method.

```python
odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)
```

We can also use + operator to combine two lists. This is also called concatenation.

The * operator repeats a list for the given number of times.

```python
odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

#Output: ["re", "re", "re"]
print(["re"] * 3)
```

Furthermore, we can insert one item at a desired location by using the method `insert()` or insert multiple items by squeezing it into an empty slice of a list.

```python
odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9] 
print(odd)

odd[2:2] = [5, 7]

# Output: [1, 3, 5, 7, 9]
print(odd)
```

### How to delete or remove elements from a list?

We can delete one or more items from a list using the keyword `del`. It can even delete the list entirely.

```python
my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)

# delete multiple items
del my_list[1:5]  

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list       

# Error: List not defined
print(my_list)
```

We can use `remove()` method to remove the given item or `pop()` method to remove an item at the given index.

The `pop()` method removes and returns the last item if index is not provided. This helps us implement lists as stacks (first in, last out data structure).

We can also use the `clear()` method to empty a list.

```python
my_list = ['p','r','o','b','l','e','m']
my_list.remove('p')

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'o'
print(my_list.pop(1))

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)

# Output: 'm'
print(my_list.pop())

# Output: ['r', 'b', 'l', 'e']
print(my_list)

my_list.clear()

# Output: []
print(my_list)
```

Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

```python
my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []
my_list				#['p', 'r', 'b', 'l', 'e', 'm']
my_list[2:5] = []
my_list				#['p', 'r', 'm']
```

## Other List Operations in Python

### List Membership Test

We can test if an item exists in a list or not, using the keyword `in`.

```python
my_list = ['p','r','o','b','l','e','m']

# Output: True
print('p' in my_list)

# Output: False
print('a' in my_list)

# Output: True
print('c' not in my_list)
```

### Built-in Functions with List

Built-in functions like `all()`, `any()`, `enumerate()`, `len()`, `max()`, `min()`, `list()`, `sorted()` etc. are commonly used with list to perform different tasks.

| Function                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [all()](https://www.programiz.com/python-programming/methods/built-in/all) | Return True if all elements of the list are true (or if the list is empty). |
| [any()](https://www.programiz.com/python-programming/methods/built-in/any) | Return True if any element of the list is true. If the list is empty, return False. |
| [enumerate()](https://www.programiz.com/python-programming/methods/built-in/enumerate) | Return an enumerate object. It contains the index and value of all the items of list as a tuple. |
| [len()](https://www.programiz.com/python-programming/methods/built-in/len) | Return the length (the number of items) in the list.         |
| [list()](https://www.programiz.com/python-programming/methods/built-in/list) | Convert an iterable (tuple, string, set, dictionary) to a list. |
| [max()](https://www.programiz.com/python-programming/methods/built-in/max) | Return the largest item in the list.                         |
| [min()](https://www.programiz.com/python-programming/methods/built-in/min) | Return the smallest item in the list                         |
| [sorted()](https://www.programiz.com/python-programming/methods/built-in/sorted) | Return a new sorted list (does not sort the list itself).    |
| [sum()](https://www.programiz.com/python-programming/methods/built-in/sum) | Return the sum of all elements in the list.                  |

