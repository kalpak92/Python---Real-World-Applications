# Python Shallow Copy and Deep Copy

## Copy in Python

You might be familiar with assignment operator `=`. In many programming languages, we use `=` operator to create a copy of an object of same data type.

Similarly, you can also create copy in Python using `=` operator. However, it doesn't create a copy of object whereas it only creates a new variable which shares the reference of the same object.

Let's take an example where we create a list named old_list and pass an object reference to new_list using `=` operator.

```python
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))
```

When we run above program, the output will be:

```python
Old List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of Old List: 140673303268168

New List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ID of New List: 140673303268168
```

As you can see from the output both variables old_list and new_list shares the same id i.e `140673303268168`.

So, if you want to modify any values in new_list or old_list, the change is visible in both.

------

Essentially, sometimes you may want to have the original values unchanged and only modify the new values or vice versa. In Python, there are two ways to create copies:

1. Shallow Copy
2. Deep Copy

To make these copy work, we use the `copy` module.

## Copy Module

We use the `copy` module of Python for shallow and deep copy operations. Suppose, you need to copy the compound list say x. For example:

```
import copy
copy.copy(x)
copy.deepcopy(x)
```

Here, the `copy()` return a shallow copy of x. Similarly, `deepcopy()` return a deep copy of x.

## Shallow Copy

A shallow copy creates a new object which stores the reference of the original elements.

So, a shallow copy doesn't create a copy of nested objects, instead it just copies the reference of nested objects. This means, a copy process does not recurse or create copies of nested objects itself.

### Create a copy using shallow copy

```python
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```

When we run the program , the output will be:

```python
Old list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
New list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

In above program, we created a nested list and then shallow copy it using `copy()` method.

This means it will create new and independent object with same content. To verify this, we print the both old_list and new_list.

To confirm that new_list is different from old_list, we try to add new nested object to original and check it.

### Adding [4, 4, 4] to old_list, using shallow copy

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)
```

When we run the program, it will output:

```python
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

In the above program, we created a shallow copy of old_list. The new_list contains references to original nested objects stored in old_list. Then we add the new list i.e `[4, 4, 4]` into old_list. This new sublist was not copied in new_list.

However, when you change any nested objects in old_list, the changes appear in new_list.

### Adding new nested object using Shallow copy

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
```

When we run the program, it will output:

```python
Old list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
```

In the above program, we made changes to old_list i.e `old_list[1][1] = 'AA'`. Both sublists of old_list and new_list at index `[1][1]` were modified. This is because, both lists share the reference of same nested objects.

------

## Deep Copy

A deep copy creates a new object and recursively adds the copies of nested objects present in the original elements.

Let’s continue with example 2. However, we are going to create deep copy using `deepcopy()`function present in `copy` module. The deep copy creates independent copy of original object and all its nested objects.

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
```

When we run the program, it will output:

```python
Old list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

In the above program, we use `deepcopy()` function to create copy which looks similar.

However, if you make changes to any nested objects in original object old_list, you’ll see no changes to the copy new_list.

### Adding a new nested object in the list using Deep copy

```python
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
```

When we run the program, it will output:

```
Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
```

In the above program, when we assign a new value to old_list, we can see only the old_list is modified. This means, both the old_list and the new_list are independent. This is because the old_list was recursively copied, which is true for all its nested objects.

## Conclusion

Normal assignment operations will simply point the new variable towards the existing object. The [docs](http://docs.python.org/2/library/copy.html) explain the difference between shallow and deep copies:

> The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
>
> - A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
> - A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Here's a little demonstration:

```python
import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
```

Using normal assignment operatings to copy:

```python
d = c

print id(c) == id(d)          # True - d is the same object as c
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
```

Using a shallow copy:

```python
d = copy.copy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # True - d[0] is the same object as c[0]
```

Using a deep copy:

```python
d = copy.deepcopy(c)

print id(c) == id(d)          # False - d is now a new object
print id(c[0]) == id(d[0])    # False - d[0] is now a new object
```

