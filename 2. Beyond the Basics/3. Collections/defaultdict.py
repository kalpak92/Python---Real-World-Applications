from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
	d[k].append(v)

print(d.items())

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
	d[k].add(v)

print(d.items())

s = 'mississippi'
d = defaultdict(int)
for k in s:
	d[k] += 1

print(d.items())