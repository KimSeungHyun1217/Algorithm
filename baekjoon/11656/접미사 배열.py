import sys

input = sys.stdin.readline

word = input()[:-1]

check = []

for i in range(len(word)):
    check.append(word[i:])
check.sort()

for i in check:
    print(i)
