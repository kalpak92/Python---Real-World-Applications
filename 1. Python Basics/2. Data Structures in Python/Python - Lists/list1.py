colors = ['red', 'blue', 'green']
print (colors[0])    ## red
print (colors[2])    ## green

print (len(colors))  ## 3

b = colors
print(b)

#Negative Indexing
print("Negative Indexing : ", b[-1])
print(b[-2:])
print("Trying to slice from right to left : ", b[-1:-2]) #No Result as python cannot from right to left.

#List Slicing
print("Sliced Content : ", colors[0:2])

#All the functions that can be applied to a list
print(dir(colors))