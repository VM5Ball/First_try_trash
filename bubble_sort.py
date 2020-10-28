#Сортировка списка А методом пузырька-
#сравниваем пары, относя последний в конец

n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())

b=[x for x in a]

def bubble_sort(a):
    n = len(a)
    for bypass in range(1, n):
        for i in range(0, n-bypass):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    print(a)

print(a)
bubble_sort(b)
