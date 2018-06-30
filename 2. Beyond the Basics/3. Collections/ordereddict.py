# Normal dictionary : Entries are retrieved in an unpredictable order

print ("Normal Dictionary")
colours =  {"Red" : 198, "Green" : 250, "Blue" : 160}
for key, value in colours.items():
    print(key, value)

from collections import OrderedDict

# Ordered Dictionary : Insertion order is preserved
print ("\nOrdered Dictionary")
colours = OrderedDict([("Red", 198), ("Green", 250), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)

# A Python program to demonstrate working of deletion
# re-inserion in OrderedDict

print("\nOrdered Dictionary Deletion\nBefore deleting:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deleting:\n")
od.pop('c')
for key, value in od.items():
    print(key, value)

print ("\nUsing popitem with last=True to pop out the last item of the dictionary")
print (od.popitem(last=True))

print("\nAfter re-inserting:\n")
od['c'] = 3
for key, value in od.items():
    print(key, value)