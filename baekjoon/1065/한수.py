def hansu(a: list):
    number = 0
    for i in a:
        save = i
        arr = []
        for j in range(len(str(i))):
            arr.append(save%10)
            save = save // 10
        compare =[]

        for h in range(len(arr)-1):
            compare.append(arr[h]-arr[h+1])

        compare = list(set(compare))

        if len(compare) <= 1:
            number += 1
    return number

b= int(input())

a = list(range(1,b+1))

print(hansu(a))








