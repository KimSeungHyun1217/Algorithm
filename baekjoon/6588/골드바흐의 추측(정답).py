import sys
check = [True for i in range(1000001)]

for i in range(2, 1001):
    if check[i]:
        for k in range(i + i, 1000001, i):
            check[k] = False



input = sys.stdin.readline

num = int(input())

while num != 0:
    for i in range(3, len(check)):
        if check[i] and check[num-i]:
            print(num, "=", i, "+", num-i)
            break
    num=int(input())