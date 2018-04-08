from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

print("\nMathematical Operations")

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print("c = ", c)
print("d = ", d)

c + d                       # add two counters together:  c[x] + d[x]
print("\nAddition:\t",Counter({'a': 4, 'b': 3}))

c - d                       # subtract (keeping only positive counts)
print("Subtraction:\t",Counter({'a': 2}))

c & d                       # intersection:  min(c[x], d[x])
print("Intersection:\t",Counter({'a': 1, 'b': 1}))

c | d                       # union:  max(c[x], d[x])
print("Union:\t",Counter({'a': 3, 'b': 2}))