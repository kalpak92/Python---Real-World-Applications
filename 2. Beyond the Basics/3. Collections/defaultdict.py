from collections import defaultdict

print ("\nDefaultdict - List")
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
	d[k].append(v)

print (d)           # Printing only the default dictionary also prints the class details
print(d.items())

print ("\nDefaultdict - Set")
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
	d[k].add(v)     #Note: we add the items to the set, not append.

print(d.items())

# Setting the default_factory to int makes the defaultdict useful for counting 
# (like a bag or multiset in other languages):
print ("\nDefaultdict - Counting")
s = 'mississippi'
d = defaultdict(int)
for k in s:
	d[k] += 1

print(d.items())