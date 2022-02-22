

a = int(input())
flag = True
for i in range(1,a+1):
    slice = i
    sum = i
    for j in range(len(str(i))):
        sum = sum + slice % 10
        slice = slice // 10
    if sum == a:
        print(i)
        flag = False
        break

if flag:
    print("0")