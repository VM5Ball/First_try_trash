a=[1, 3, 4, 6, 89]
b=[x for x in a]
c=[x for x in a]

def my_sorted(a):
    flag = True
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            flag = False
    return flag        

def check_sorted(a, ascending=True):
    flag = True
    s = 2*int(ascending)-1
    for i in range(len(a)-1):
        if s*a[i]>s*a[i+1]:
            flag = False
            break
    return flag    

print(check_sorted(b))
print(my_sorted(c))
