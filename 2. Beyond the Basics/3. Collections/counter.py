from collections import Counter

print ("Counter from an iterable",Counter('gallahad'))                 # a new counter from an iterable
print ("Counter from a dictionary",Counter({'red': 4, 'blue': 2}))      # a new counter from a mapping
print ("Counter from keyword args",Counter(cats=4, dogs=8))             # a new counter from keyword args

'''
Counter allows us to count the occurrences of a particular item.
For instance it can be used to count the number of individual favourite colours.
'''
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

# counting the names from a tuple of tuple.
favs = Counter(name for name, colour in colours)
print('\n',favs)

print("\nMathematical Operations")

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print("c = ", c)
print("d = ", d)

c + d                       # add two counters together:  c[x] + d[x]
print("\nAddition:\t",c + d)

c - d                       # subtract (keeping only positive counts)
print("Subtraction:\t",c - d)

c & d                       # intersection:  min(c[x], d[x])
print("Intersection:\t",c & d)

c | d                       # union:  max(c[x], d[x])
print("Union:\t",c | d)

print ("\nCounting the most common words in a paragraph")
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print (Counter(words))
print ("\nMost Common 5 words",Counter(words).most_common(5))
n = 5
print ("\nLeast common 5 words",Counter(words).most_common()[:-n-1:-1])       # n least common elements
