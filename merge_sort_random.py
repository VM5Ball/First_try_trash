from random import randint
from sys import argv

try:
    k = int(argv[1])
except:
    k = 10

a = [randint(1, 100) for x in range(k)]    


def merge_sort(a):             
    if len(a) <= 1: 
        return a     
    middle = len(a) // 2   
    left = merge_sort(a[:middle]) 
    right = merge_sort(a[middle:])
    return merge(left, right) 
                             

def merge(left, right):
    result = []   
    while len(left) > 0 and len(right) > 0: 
        if left[0] <= right[0]:             
            result.append(left[0]) 
            left = left[1:]  
        else:
            result.append(right[0]) 
            right = right[1:] 
    if len(left) > 0:
        result += left 
    if len(right) > 0: 
        result += right 
    return result

print(a)
b = merge_sort(a)
print(b)
    
