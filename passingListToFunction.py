def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd
lst = [12, 6, 78, 25, 19, 13, 45]
even, odd = count(lst)
print ("even: {} odd: {}".format(even, odd ))