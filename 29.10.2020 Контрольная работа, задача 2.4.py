from random import randint
import random
n=randint(12,30)  #рандомно создаётся количество студентов в группе
print('Students in a group: ', n)
m=3 #количество оценок каждого студента, 3 потому что 3 предмета
spisok=[]

for i in range(n):
	spisok_k=random.sample((0,2,3,4,5), 3)
	spisok.append(spisok_k)
	spisok_k=[]
for x in spisok:
	print(x)

kol_neyavok=0 #количество неявок по информатике
kol_neud=0 #количесвто неудовлетворительных оценок по информатике
kol_ud=0 #количество удовлетворительных оценок по информатике
kol_khorosh=0 #количество хороших оценок по информатике
kol_otlich=0 #количество отличных оценок по информатике

for person in spisok:
	if person[2]==0:
		kol_neyavok+=1
	if person[2]==2:
		kol_neud+=1
	if person[2]==3:
		kol_ud+=1
	if person[2]==4:
		kol_khorosh+=1
	if person[2]==5:
		kol_otlich+=1
'''
print('количество неявок по информатике: ',kol_neyavok)
print('количесвто неудовлетворительных оценок по информатике: ',kol_neud)
print('количество удовлетворительных оценок по информатике: ',kol_ud)
print('количество хороших оценок по информатике: ',kol_khorosh)
print('количество отличных оценок по информатике: ',kol_otlich)
'''
print('Amount of students absent: ',kol_neyavok)
print('Amount of students with unacceptable mark: ',kol_neud)
print('Amount of students with acceptable mark: ',kol_ud)
print('Amount of students with good mark: ',kol_khorosh)
print('Amount of students with excellent mark: ',kol_otlich)