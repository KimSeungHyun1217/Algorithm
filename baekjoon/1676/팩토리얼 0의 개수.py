import sys

input = sys.stdin.readline

num = int(input())
x = 1
for i in range(1,num+1):
    x = x * i
print(x)
num = 0
for i in range(len(str(x))):
    if x % 10 == 0:
        num += 1
        x //= 10
        print(x)
    else:
        break

print(num)