a = int(input())

while a!=0:
    check = 0
    arr = [True] * (2*a+1)
    for i in range(2,2*a+1):
        if arr[i]:
            if i > a: check += 1
            for j in range(2*i,2*a+1,i):
                arr[j] = False

    print(check)
    a = int(input())