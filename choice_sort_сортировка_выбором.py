#Cортировка списка А выбором
#-на первый ставим минимум
#и сравниваем всех с минимумом



n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(input())
    
b=[x for x in a]

def choice_sort(a):
    n = len(a)
    for pos in range(0, n-1):
        for i in range(pos+1, n):
            if a[i] < a[pos]:
                a[i], a[pos] = a[pos], a[i]
    print(a)

print(a)
choice_sort(b) 
