# Python Closures

## nonlocal

The use of `nonlocal` keyword is very much similar to the `global` keyword. `nonlocal` is used to declare that a variable inside a nested function (function inside a function) is not local to it, meaning it lies in the outer inclosing function. If we need to modify the value of a non-local variable inside a nested function, then we must declare it with `nonlocal`. Otherwise a local variable with that name is created inside the nested function. Following example will help us clarify this.

```python
def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()
```

**Output**

```python
Inner function:  10
Outer function:  10
```

Here, the `inner_function()` is nested within the `outer_function`.

The variable a is in the `outer_function()`. So, if we want to modify it in the `inner_function()`, we must declare it as `nonlocal`. Notice that a is not a global variable.

Hence, we see from the output that the variable was successfully modified inside the nested `inner_function()`. The result of not using the `nonlocal` keyword is as follows:

```python
def outer_function():
    a = 5
    def inner_function():
        a = 10
        print("Inner function: ",a)
    inner_function()
    print("Outer function: ",a)

outer_function()
```

**Output**

```python
Inner function:  10
Outer function:  5
```

Here, we do not declare that the variable a inside the nested function is `nonlocal`. Hence, a new local variable with the same name is created, but the non-local a is not modified as seen in our output.

### Nonlocal variable in a nested function

Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.

A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.

In Python, these non-local variables are read only by default and we must declare them explicitly as non-local (using [nonlocal keyword](https://www.programiz.com/python-programming/keyword-list#nonlocal)) in order to modify them.

Following is an example of a nested function accessing a non-local variable.

```python
def print_msg(msg):
# This is the outer enclosing function

    def printer():
	# This is the nested function
        print(msg)

    printer()

# We execute the function
# Output: Hello
print_msg("Hello")
```

Output:

```python
Hello
```

We can see that the nested function `printer()` was able to access the non-local variable msg of the enclosing function.

## Defining a Closure Function

In the example above, what would happen if the last line of the function `print_msg()`returned the `printer()` function instead of calling it? This means the function was defined as follows:

```python
def print_msg(msg):
# This is the outer enclosing function

    def printer():
    # This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()
```

Output:

```python
Hello
```

That's unusual.

The `print_msg()` function was called with the string `"Hello"` and the returned function was bound to the name another. On calling `another()`, the message was still remembered although we had already finished executing the `print_msg()` function.

This technique by which some data (`"Hello"`) gets attached to the code is called **closure in Python**.

This value in the enclosing scope is remembered even when the variable goes out of scope or the function itself is removed from the current namespace.

## When do we have a closure?

As seen from the above example, we have a closure in Python when a nested function references a value in its enclosing scope.

The criteria that must be met to create closure in Python are summarized in the following points.

- We must have a nested function (function inside a function).
- The nested function must refer to a value defined in the enclosing function.
- The enclosing function must return the nested function.

## When to use closures?

So what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.

Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.

```python
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
```

Output:

27
15
30

Decorators in Python make an extensive use of closures as well.

On a concluding note, it is good to point out that the values that get enclosed in the closure function can be found out.

All function objects have a `__closure__` attribute that returns a tuple of cell objects if it is a closure function. Referring to the example above, we know `times3` and `times5` are closure functions.

```python
>>> make_multiplier_of.__closure__
>>> times3.__closure__
(<cell at 0x0000000002D155B8: int object at 0x000000001E39B6E0>,)
```

The cell object has the attribute cell_contents which stores the closed value.

```python
>>> times3.__closure__[0].cell_contents
3
>>> times5.__closure__[0].cell_contents
5
```