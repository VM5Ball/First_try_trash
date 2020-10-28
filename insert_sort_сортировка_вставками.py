#Cортировка списка А вставками-
#берём элемент и несём влево
#пока он меньше того кто перед ним

n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())

b=[x for x in a]

def insert_sort(a):
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k-=1
    print(a)        


print(a)    
insert_sort(b)
