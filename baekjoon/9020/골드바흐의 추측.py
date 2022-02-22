def isFrime(num):
    if num ==1: return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0: return False
    return True


a = int(input())

for i in range(a):
    b = int(input())

    for i in range(b//2):
        if b == (b//2 -i) + (b//2 + i):
            if isFrime(b//2-i) and isFrime(b//2 +i):
                print(b//2-i,b//2+i)
                break

