import sys

input = sys.stdin.readline

check = [0 for _ in range(26)]

word = input()[:-1]

for i in word:
    check[ord(i)-97] += 1

print(*check)