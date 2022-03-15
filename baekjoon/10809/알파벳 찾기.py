import sys

input = sys.stdin.readline

check = [-1 for _ in range(26)]

word = input()[:-1]

for i in range(len(word)):
    if check[ord(word[i])-97] == -1:
        check[ord(word[i]) - 97] = i


print(*check)