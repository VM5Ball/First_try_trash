#есть последовательность, разбиваем на 2 части
#пока не будет в каждом подмассиве по 1 элементу
#оследоватьельно сравниваем по 2 элемента
#дальше берём пары, сравниваем первые элементы
#дальше берём четверки и последоваттельно 
#сравниваем первые, потом вторые , потом третьи тд


n=int(input())
a = [0]*n
for i in range(n):
    a[i]=int(input())

def merge_sort(a):             
    if len(a) <= 1: #если длина подмасиива равна 1
        return a     #то возвращаем его
    middle = len(a) // 2   #иначе делим пополам
    left = merge_sort(a[:middle]) #сортируем левую и правую
    right = merge_sort(a[middle:])#части той же функцией 
    return merge(left, right) # возвращаем результат слияния 
                             # двух отсортированных последовательностей

def merge(left, right): #берёт на вход 2 отсортированных послеовательности
    result = []   #результаттом будем послежовательность
    while len(left) > 0 and len(right) > 0: #пока влевой и правой есть
        if left[0] <= right[0]:             
            result.append(left[0]) #добавляем левый если он меньше
            left = left[1:]  #убираем его из последовательности
        else:
            result.append(right[0]) #добавляем правый если меньше
            right = right[1:] #убираем правый из последовательности
    if len(left) > 0: #если правая пустая, то 
        result += left #к результату добавляем другую
    if len(right) > 0: #если левая уже пустая, а правая нет
        result += right #то добавляем к результату правую
    return result

print(a)
b = merge_sort(a)
print(b)
    
        
        
