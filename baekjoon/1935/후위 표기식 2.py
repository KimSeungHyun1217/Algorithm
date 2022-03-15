import sys
from collections import Counter
input = sys.stdin.readline

num = int(input())
check =[]
word = list(input().strip())

for i in range(num):
    check.append(int(input()))

num =[]


for i in word:
    if i.isalpha():
        num.append(check[ord(i)-ord('A')])
    else:
        x = num.pop()
        y = num.pop()

        if i == '+':
            num.append(x+y)
        elif i == '-':
            num.append(y-x)
        elif i == '*':
            num.append(y*x)
        elif i == '/':
            num.append(y/x)
print(f"{num[0]:.2f}")

