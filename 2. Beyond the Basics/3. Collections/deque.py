from collections import deque

d = deque()
d.append('1')
d.append('2')
d.append('3')
d.append(4)

print("A Simple deque: ",d)

print ("\n********************************************************\n")
d = deque(range(5))
print("The deque is :", d, "and Length of deque is: ", len(d))
print("PopLeft : ", d.popleft())
print("deque is :", d)
print("Pop : ", d.pop())
print("deque is :", d)

print ("\n*********************************************************\n")
d = deque([1,2,3,4,5])
d.extendleft([0])
print ("Extending Left",d)
d.extend([6,7,8])
print("Extending right",d)

d.rotate(1)		#right rotation
print("Deque Right rotation : ", d)

d.rotate(-1)	#left rotation
print("Deque Left rotation : ", d)