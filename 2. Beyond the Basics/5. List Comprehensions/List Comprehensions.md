# Python List Comprehension

List comprehension is powerful and must know concept in Python. Yet, this remains one of the most challenging topic for beginners. Mastering this concept would help you in two ways:

1. You would start writing shorter and effective codes
2. Hence, your code will execute faster

Do you know List Comprehensions are 35% faster than FOR loop and 45% faster than map function?

## What is List Comprehension (LC)?

When I first used LC, it took me down the memory lane and reminded me of the **set-builder form.** Yes you got me right. Lets look at some of basic examples:

1. { x^2: x is a natural number less than 10 }
2. { x: x is a whole number less than 20, x is even }
3. { x: x is an alphabet in word ‘MATHEMATICS’, x is a vowel }

Now let’s look at the corresponding Python codes implementing LC (in the same order):

1. ```python
   [x**2 for x in range(0,10)]	
   ```

2. ```python
   [x for x in range(1,20) if x%2==0 ]
   ```

3. ```python
   [x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']]
   ```

Each of the above example involves 3 things – **iteration, conditional filtering and processing**. Hence, you might say its just another representation of FOR loop.

In a general sense, a FOR loop works as:

```python
for (set of values to iterate):
  if (conditional filtering): 
    output_expression()
```

```python
The same gets implemented in a simple LC construct in a single line as:
 [ output_expression() for(set of values to iterate) if(conditional filtering) ]
```

Consider another example: { x: x is a natural number less than or equal to 100, x is a perfect square }
This can be solved using a for-loop as:

```python
for i in range(1,101):     #the iterator
   if int(i**0.5)==i**0.5: #conditional filtering
     print i               #output-expression
```

Now, to create the LC code, we need to just plug in the different parts:

```python
[i for i in range(1,101) if int(i**0.5)==i**0.5]
```

 LC is a simple but powerful technique and can help you accomplish a variety of tasks with ease. Things to keep in mind:

1. LC will always return a result, whether you use the result or nor.
2. The iteration and conditional expressions can be nested with multiple instances.
3. Even the overall LC can be nested inside another LC.
4. Multiple variables can be iterated and manipulated at same time.

Let’s look at some more examples to understand this in detail.

### Example 1: Flatten a Matrix

**Aim:** Take a matrix as input and return a list with each row placed on after the other.

Python codes with FOR-loop and LC implementations:

```python
def eg1_for(matrix):
    flat = []
    for row in matrix:
        for x in row:
            flat.append(x)
    return flat

def eg1_lc(matrix):
    return [x for row in matrix for x in row ]
```

Let’s define a matrix and test the results:

```python
matrix = [ range(0,5), range(5,10), range(10,15) ]
print "Original Matrix: " + str(matrix)
print "FOR-loop result: " + str(eg1_for(matrix))
print "LC result      : " + str(eg1_lc(matrix))
```

Output:

[![eg1_output](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/eg1_output.png)](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/eg1_output.png)

### Example 2: Removing vowels from a sentence

**Aim:** Take a string as input and return a string with vowels removed.

Python codes with FOR-loop and LC implementations:

```python
def eg2_for(sentence):
    vowels = 'aeiou'
    filtered_list = []
    for l in sentence:
        if l not in vowels:
            filtered_list.append(l)
    return ''.join(filtered_list)

def eg2_lc(sentence):
    vowels = 'aeiou'
    return ''.join([ l for l in sentence if l not in vowels])
```

Let’s define a matrix and test the results:

```python
sentence = 'My name is Aarshay Jain!'
print "FOR-loop result: " + eg2_for(sentence)
print "LC result      : " + eg2_lc(sentence)
```

Output:

[![eg2_output](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/eg2_output.png)](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/eg2_output.png)

### Example 3: Dictionary Comprehension

**Aim:** Take two list of same length as input and return a dictionary with one as keys and other as values.

Python codes with FOR-loop and LC implementations:

```python
def eg3_for(keys, values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    return dic

def eg3_lc(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }
```

Let’s define a matrix and test the results:

```python
country = ['India', 'Pakistan', 'Nepal', 'Bhutan', 'China', 'Bangladesh']
capital = ['New Delhi', 'Islamabad','Kathmandu', 'Thimphu', 'Beijing', 'Dhaka']
print "FOR-loop result: " + str(eg3_for(country, capital))
print "LC result      : " + str(eg3_lc(country, capital))
```

Output:

[![eg3_output](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/eg3_output.png)](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/eg3_output.png)

## The Time advantage

In this section, we will find out the time taken by LC in comparison to similar techniques. We will also try to unravel the situations in which LC works better and where it should be avoided. Along with runtime, we will compare the readability of the different approaches.

Before jumping into comparing the time taken by different techniques, lets take a refresher on the Python map function.

### map function

It is used to apply a function to each element of a list or any other iterable.
**Syntax: map(function, Python iterable)**

For example, we can multiply each element of a list of integers with the next number using the following code: 

```python
map(lambda x: x*(x+1), arr)
```

### Comparing Runtime

An important part of this exercise is the ability to compare the running time of a code fragment. We will be using **%timeit**, an in-built magic function of iPython notebook environment. Alternatively, you can use the time or timeit modules.

### A Simple Example

Lets start with a simple example – squaring each element of a list. The Python codes and runtimes for each of the 3 implementations are:

```python
#Method 1: For-Loop
def square_for(arr):
    result = []
    for i in arr:
        result.append(i**2)
    return result
%timeit square_for(range(1,11))
```

Output:

```python
4.08 µs ± 50.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

```python
#Method 2: Map Function
def square_map(arr):
    return map(lambda x: x**2, arr)
%timeit square_map(range(1,11))
```

Output:

```python
661 ns ± 1.74 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

```python
#Method 3: List comprehension:
def square_lc(arr):
    return [i**2 for i in arr]
%timeit square_lc(range(1,11))
```

Output:

```python
3.57 µs ± 73.3 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

**Readability:** Both LC and map functions are fairly simple and readable, but for-loop is a bit bulky but not much.

So can we say LC is the fastest method? Not necessary! We can’t generalize our conclusions at this stage as it might be specific to the problem at hand. 

Remember:

- When all you’re doing is calling an already-defined function on each element, `map(f, lst)` is a little faster than the corresponding list comprehension `[f(x) for x in lst]`. To an experienced Python programmer, I think it’s clearer, too (though [Guido](https://www.quora.com/topic/Guido-van-Rossum-1) may disagree).

- But when evaluating any other expression, `[some_expr for x in lst]`is faster and clearer than `map(lambda x: some_expr, lst)`, because the `map` incurs an extra function call for each element.

  It’s also worth mentioning that Python 3’s `map` returns a generator (like Python 2’s `itertools.imap`) instead of a list.

Let’s consider a slightly tricky example.

### Taking a step forward

Let’s include a catch in above problem. What if we want the square of only even numbers in the list? Now, the three functions would look like:

```python
#Method 1: For-Loop
def square_even_for(arr):
    result = []
    for i in arr:
        if i%2 == 0:
            result.append(i**2)
    return result
%timeit square_even_for(range(1,11))
```

Output:

```python
2.83 µs ± 15.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

```python
#Method 2: Map Function
def square_even_map(arr):
    return filter(lambda x: x is not None,map(lambda x: x**2 if x%2==0 else None, arr))
%timeit square_even_map(range(1,11))
```

Output:

```python
891 ns ± 10.3 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
```

```python
#Method 3: List comprehension:
def square_even_lc(arr):
    return [i**2 for i in arr if i%2==0]
%timeit square_even_lc(range(1,11))
```

Output:

```python
2.66 µs ± 34.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```

**Readability:** LC is most concise and elegant. Map function became cumbersome with additional lambda function and for-loop is no better.

Let’s summarize our findings now:

1. LC is **fast and elegant in cases where simple expressions are involved**. But if complex functions are required, map and LC would perform nearly the same
2. FOR-loop is bulkier in general, but it is fastest if storing is not required. So should be **preferred in cases where we need to simply iterate and perform operations.**

I have compared the runtime of 3 examples we saw earlier and the results are:
[![runtime comparison](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/runtime-comparison.png)](https://www.analyticsvidhya.com/wp-content/uploads/2016/01/runtime-comparison.png)

