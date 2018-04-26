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