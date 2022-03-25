import sys

def isPrime(num):
    checklist= []
    for j in range(2,num+1):
        check = True
        for i in range(2 , int(j**0.5) + 1):
            if j % i ==0:
                check = False
                break
        if check:
            checklist.append(j)
    
    if len(checklist) <2 :
        return "Goldbach's conjecture is wrong."
    check = 0
    a=b=0
    for i in range(len(checklist)):
        for j in range(i+1,len(checklist)):
            if checklist[i]+checklist[j] == num:
                if abs(i-j) > check:
                    a = checklist[i]
                    b = checklist[j]
                    check = abs(i-j)

    if a ==0:
        return "Goldbach's conjecture is wrong."
    if a>b:
        temp = a
        a = b
        b = temp
    return f"{num} = {a} + {b}"
            
        



input = sys.stdin.readline

num = int(input())

while num != 0:
    print(isPrime(num))
    num=int(input())