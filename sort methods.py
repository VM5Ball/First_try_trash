def insert_sort(a):
    '''Cортировка списка А вставками-
    берём элемент и несём влево
    пока он меньше того кто перед ним'''
    n = len(a)
    for top in range(1, n):
        k = top
        while k > 0 and a[k-1] > a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k-=1

def choice_sort(a):
    '''Cортировка списка А выбором
       -на первый ставим минимум
       и сравниваем всех с минимумом'''
    n = len(a)
    for pos in range(0, n-1):
        for i in range(pos+1, n):
            if a[i] < a[pos]:
                a[i], a[pos] = a[pos], a[i]

def bubble_sort(a):
    ''' Сортировка списка А методом пузырька-
    сравниваем пары, относя последний в конец'''
    n = len(a)
    for bypass in range(1, n):
        for i in range(0, n-bypass):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]

def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    a = [4, 2, 5, 1, 3]
    a_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(a)
    print('ok' if a == a_sorted else 'fail')

    print('testcase #2: ', end='')
    a = list(range(10,20)) + list(range(0,10)) 
    a_sorted = list(range(20))
    sort_algorithm(a)
    print('ok' if a == a_sorted else 'fail')

    print('testcase #3: ', end='')
    a = [4, 2, 4, 2, 1]
    a_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(a)
    print('ok' if a == a_sorted else 'fail')


if  __name__== '__main__':
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
    
    
