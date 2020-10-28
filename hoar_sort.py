a=[23, -3, 123, -34, -55, 12, 9]

b=[x for x in a]

def hoar_sort(a):
    if len(a)<=1:
        return
    barrier = a[0]
    left=[]
    right=[]
    mid=[]
    for x in a:
        if x<barrier:
            left.append(x)
        elif x == barrier:
            mid.append(x)
        else:
            right.append(x)
    hoar_sort(left)
    hoar_sort(right)
    k=0
    for x in left+mid+right:
        a[k]=x
        k+=1

print(a)
hoar_sort(b)
print(b)
                        
