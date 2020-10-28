from random import randint
x=''
a1=str(randint(0,9))
a2=str(randint(0,9))
a3=str(randint(0,9))
a4=str(randint(0,9))
while a1==a2 or a1==a3 or a1==a4 or a2==a3 or a2==a4 or a3==a4:
    a1=str(randint(0,9))
    a2=str(randint(0,9))
    a3=str(randint(0,9))
    a4=str(randint(0,9))
x=a1+a2+a3+a4 
#print('Number to guess: ', x)
bik=kor=0
print('Enter your number: ')
v=str(input())
while x!=v:
    bik=kor=0
    for i in range(4):
        for j in range(4):
            if x[i]==v[j]:
                if i!=j:
                    kor+=1
                if i==j:
                    bik+=1
    print('Bulls: ', bik)
    print('Cows: ', kor)
    print('Enter another number')
    v=str(input())
print('You won the game!')    