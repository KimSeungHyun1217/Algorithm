import sys
from collections import deque
input = sys.stdin.readline

sentence = input().strip()

queue = deque()
stack_list =[]
flag = None
for i in sentence:
    if i == "<":
        if stack_list:
            for _ in range(len(stack_list)):
                queue.append(stack_list.pop())
        queue.append(i)
        flag = True
    elif i == ">":
        queue.append(i)
        flag = False
    elif i == " ":
        for _ in range(len(stack_list)):
            queue.append(stack_list.pop())
        queue.append(" ")

    else:
        if flag == True:
            queue.append(i)
        else:
            stack_list.append(i)

if stack_list:
    for _ in range(len(stack_list)):
        queue.append(stack_list.pop())

for _ in range(len(queue)):
    print(queue.popleft(),end="")