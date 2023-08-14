from numpy import *
arr = array([8,20,12,4])
tmp = arr[0]
i = 0
for i in range(4):
    if(arr[i]>tmp):
        tmp = arr[i]
print(tmp)
