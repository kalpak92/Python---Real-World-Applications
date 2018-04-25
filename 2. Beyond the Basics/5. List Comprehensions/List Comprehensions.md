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

