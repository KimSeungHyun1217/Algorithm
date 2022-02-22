import sys

input = sys.stdin.readline
num = int(input())

for i in range(num):
    word = input()


    for j in word.strip().split(" "):
        stack_list = []
        for k in list(j):
            stack_list.append(k)
        for c in range(len(stack_list)):
            print(stack_list.pop(),end="")
        print(end=" ")


