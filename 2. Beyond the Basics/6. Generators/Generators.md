# Python Iterators

According to Wikipedia, an iterator is an object that enables a programmer to traverse a container, particularly lists. However, an iterator performs traversal and gives access to data elements in a container, but does not perform iteration. You might be confused so lets take it a bit slow. There are three parts namely:

- Iterable
- Iterator
- Iteration

All of these parts are linked to each other. We will discuss them one by one and later talk about generators.

## Iterable

An `iterable` is any object in Python which has an `__iter__` or a `__getitem__` method defined which returns an **iterator** or can take indexes. In short an `iterable` is any object which can provide us with an **iterator**. 

So what is an **iterator**?

## Iterator

An iterator is any object in Python which has a `next` (Python2) or `__next__` method defined. That’s it. 

Iterators are everywhere in Python. They are elegantly implemented within `for` loops, comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an [object](https://www.programiz.com/python-programming/class) that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python **iterator object** must implement two special methods, `__iter__()`and `__next__()`, collectively called the **iterator protocol**.

An object is called **iterable** if we can get an iterator from it. Most of built-in containers in Python like: [list](https://www.programiz.com/python-programming/list), [tuple](https://www.programiz.com/python-programming/tuple), [string](https://www.programiz.com/python-programming/string) etc. are iterables.

The `iter()` function (which in turn calls the `__iter__()` method) returns an iterator from them.

## Iteration

In simple words it is the process of taking an item from something e.g a list. When we use a loop to loop over something it is called iteration. It is the name given to the process itself.

## Iterating Through an Iterator in Python

We use the `next()` function to manually iterate through all the items of an iterator. When we reach the end and there is no more data to be returned, it will raise `StopIteration`. 

Following is an example:

```python
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
next(my_iter)
```

## How for loop actually works?

As we see in the above example, the `for` loop was able to iterate automatically through the list.

In fact the `for` loop can iterate over any iterable. Let's take a closer look at how the `for`loop is actually implemented in Python.

```python
for element in iterable:
    # do something with element
```

Is actually implemented as.

```python
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

So internally, the `for` loop creates an iterator object, `iter_obj` by calling `iter()` on the iterable.

Ironically, this `for` loop is actually an infinite [while loop](https://www.programiz.com/python-programming/while-loop).

Inside the loop, it calls `next()` to get the next element and executes the body of the `for`loop with this value. After all the items exhaust, `StopIteration` is raised which is internally caught and the loop ends. Note that any other kind of exception will pass through.

## Building Your Own Iterator in Python

Building an iterator from scratch is easy in Python. We just have to implement the methods `__iter__()` and `__next__()`.

The `__iter__()` method returns the iterator object itself. If required, some initialization can be performed.

The `__next__()` method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise `StopIteration`.

Here, we show an example that will give us next power of 2 in each iteration. Power exponent starts from zero up to a user set number.

```python
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
            
a = PowTwo(4)
i = iter(a)
print (next(i))
print (next(i))
print (next(i))
print (next(i))
print (next(i))
print (next(i))
```

Output:

```python
1
2
4
8
16
Traceback (most recent call last):
  File "main.py", line 27, in <module>
    print (next(i))
  File "main.py", line 18, in __next__
    raise StopIteration
StopIteration
```

We can also use a `for` loop to iterate over our iterator class.

```python
>>> for i in PowTwo(5):
...     print(i)
...     
1
2
4
8
16
32
```

## Python Infinite Iterators

It is not necessary that the item in an iterator object has to exhaust. There can be infinite iterators (which never ends). We must be careful when handling such iterator.

Here is a simple example to demonstrate infinite iterators.

The [built-in function](https://www.programiz.com/python-programming/built-in-function) `iter()` can be called with two arguments where the first argument must be a callable object (function) and second is the sentinel. The iterator calls this function until the returned value is equal to the sentinel.

```python
>>> int()
0

>>> inf = iter(int,1)
>>> next(inf)
0
>>> next(inf)
0
```

We can see that the `int()` function always returns 0. So passing it as `iter(int,1)` will return an iterator that calls `int()` until the returned value equals 1. This never happens and we get an infinite iterator.

We can also built our own infinite iterators. The following iterator will, theoretically, return all the odd numbers.

```python
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

a = iter(InfIter())
print (next(a))
print (next(a))
print (next(a))
print (next(a))
```

Output:

```python
1
3
5
7
```

And so on...

Be careful to include a terminating condition, when iterating over these type of infinite iterators.

The advantage of using iterators is that they save resources. Like shown above, we could get all the odd numbers without storing the entire number system in memory. We can have infinite items (theoretically) in finite memory.

Iterator also makes our code look cool.

There's an easier way to create iterators in Python.

# Python Generators

## What are generators in Python?

There is a lot of overhead in building an iterator in Python, we have to implement a class with `__iter__()` and `__next__()` method, keep track of internal states, raise `StopIteration`when there was no values to be returned etc.

This is both lengthy and counter intuitive. Generator comes into rescue in such situations.

Python generators are a simple way of creating iterators. All the overhead we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

## How to create a generator in Python?

It is fairly simple to create a generator in Python. It is as easy as defining a normal function with `yield` statement instead of a `return` statement.

If a function contains at least one `yield` statement (it may contain other `yield` or `return`statements), it becomes a generator function. Both `yield` and `return` will return some value from a function.

The difference is that, while a `return` statement terminates a function entirely, `yield`statement pauses the function saving all its states and later continues from there on successive calls.

## Differences between Generator function and a Normal function

Here is how a generator function differs from a [normal function](https://www.programiz.com/python-programming/function).

- Generator function contains one or more `yield` statement.
- When called, it returns an object (iterator) but does not start execution immediately.
- Methods like `__iter__()` and `__next__()` are implemented automatically. So we can iterate through the items using `next()`.
- Once the function yields, the function is paused and the control is transferred to the caller.
- Local variables and their states are remembered between successive calls.
- Finally, when the function terminates, `StopIteration` is raised automatically on further calls.

Here is an example to illustrate all of the points stated above. We have a generator function named `my_gen()` with several `yield` statements.

```python
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
a = my_gen()
print (next(a))
print (next(a))
print (next(a))
print (next(a))
```

Output:

```python
This is printed first
1
This is printed second
2
This is printed at last
3
Traceback (most recent call last):
  File "main.py", line 20, in <module>
    print (next(a))
StopIteration
```

One interesting thing to note in the above example is that, the value of variable n is remembered between each call.

Unlike normal functions, the local variables are not destroyed when the function yields. Furthermore, the generator object can be iterated only once.

To restart the process we need to create another generator object using something like `a = my_gen()`.

**Note:** One final thing to note is that we can use generators with for loops directly.

This is because, a `for` loop takes an iterator and iterates over it using `next()` function. It automatically ends when `StopIteration` is raised. 

```python
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
# Using for loop
for item in my_gen():
    print(item) 
```

When you run the program, the output will be:

```python
This is printed first
1
This is printed second
2
This is printed at last
3
```

## Python Generators with a Loop

The above example is of less use and we studied it just to get an idea of what was happening in the background.

Normally, generator functions are implemented with a loop having a suitable terminating condition.

Let's take an example of a generator that reverses a string.

```python
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)
```

Output:

```python
o
l
l
e
h
```

In this example, we use `range()` function to get the index in reverse order using the for loop.

It turns out that this generator function not only works with string, but also with other kind of iterables like list, tuple etc.

Generators are best for calculating large sets of results (particularly calculations involving loops themselves) where you don’t want to allocate the memory for all results at the same time. Many Standard Library functions that return `lists` in Python 2 have been modified to return `generators` in Python 3 because `generators` require fewer resources.

Here is an example `generator` which calculates fibonacci numbers:

```python
# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
```

Now we can use it like this:

```python
for x in fibon(1000000):
    print(x)
```

This way we would not have to worry about it using a lot of resources. However, if we would have implemented it like this:

```python
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

It would have used up all our resources while calculating a large input.

# Python Generator Expression

Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.

Same as lambda function creates an [anonymous function](https://www.programiz.com/python-programming/anonymous-function), generator expression creates an **anonymous generator function**.

The syntax for generator expression is similar to that of a [list comprehension in Python](https://www.programiz.com/python-programming/list#list-comprehension). But the square brackets are replaced with round parentheses.

***The major difference between a list comprehension and a generator expression is that while list comprehension produces the entire list, generator expression produces one item at a time.***

They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much more memory efficient than an equivalent list comprehension.

```python
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print ([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print ((x**2 for x in my_list))
```

We can see above that the generator expression did not produce the required result immediately. Instead, it returned a generator object with produces items on demand.

```python
# Initialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
next(a)
```

Generator expression can be used inside functions. When used in such a way, the round parentheses can be dropped.

```python
sum(x**2 for x in my_list)
# Output: 146

max(x**2 for x in my_list)
# Output: 100

sum(x for x in range(10))
# Output: 45
```

# Why generators are used in Python?

There are several reasons which make generators an attractive implementation to go for.

### 1. Easy to Implement

Generators can be implemented in a clear and concise way as compared to their iterator class counterpart. Following is an example to implement a sequence of power of 2's using iterator class.

```python
class PowTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
```

This was lengthy. Now lets do the same using a generator function.

```python
def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
```

Since, generators keep track of details automatically, it was concise and much cleaner in implementation.

### 2. Memory Efficient

A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill if the number of items in the sequence is very large.

Generator implementation of such sequence is memory friendly and is preferred since it only produces one item at a time.

### 3. Represent Infinite Stream

Generators are excellent medium to represent an infinite stream of data. Infinite streams cannot be stored in memory and since generators produce only one item at a time, it can represent infinite stream of data.

The following example can generate all the even numbers (at least in theory).

```python
def all_even():
    n = 0
    while True:
        yield n
        n += 2
```

### 4. Pipelining Generators

Generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a log file from a famous fast food chain. The log file has a column (4th column) that keeps track of the number of pizza sold every hour and we want to sum it to find the total pizzas sold in 5 years.

Assume everything is in string and numbers that are not available are marked as 'N/A'. A generator implementation of this could be as follows.

```python
with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))
```

This pipelining is efficient and easy to read (and yes, a lot cooler!).