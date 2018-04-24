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

