from array import *
arr = array('i', [])
n = int(input('Please enter the length of the array: '))
for i in range(n):
    x = int(input('Please enter next value of array:  '))
    arr.append(x)
print (arr)
val = int(input('Please search the element from array: '))
print(arr.index(val))


