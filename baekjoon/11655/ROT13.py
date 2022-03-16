import sys

input = sys.stdin.readline

word = input()[:-1]
ans = ""


for i in word:
    if i.isupper():
        check = ord(i) + 13
        if check > 90:
            check -= 26
        ans += chr(check)
    elif i.islower():
        check = ord(i) + 13
        if check > 122:
            check -= 26
        ans += chr(check)
    else:
        ans += i

print(ans)