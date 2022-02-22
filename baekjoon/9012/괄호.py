import sys

input = sys.stdin.readline
num = int(input())

for i in range(num):
    stack_list = []
    flag =True
    word = input()

    for j in word.strip():
        if j == "(":
            stack_list.append(j)
        else:
            if len(stack_list) == 0:
                print("NO")
                flag= False
                break
            else:
                stack_list.pop()
    if flag:
        if len(stack_list) == 0:
            print("YES")
        else:
            print("NO")





