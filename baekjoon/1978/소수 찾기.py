import sys

input = sys.stdin.readline

num = int(input())
arr = list(map(int,input().split()))
amount = 0
for i in arr:
    num = 0
    for j in range(1,i+1):
        if i % j == 0:
           num += 1 
    if num == 2:
        amount += 1

print(amount)
