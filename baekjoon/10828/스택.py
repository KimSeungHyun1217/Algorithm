import sys

input = sys.stdin.readline

num = int(input())

stack_list = []
top = -1
for i in range(num):
    command = input()
    command = command.split()

    if command[0] == 'push':
        stack_list.append(command[1])
        top = top + 1
    elif command[0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack_list[top])
            del stack_list[top]
            top = top - 1
    elif command[0] == 'size':
        print(top + 1)
    elif command[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    else:
        if top == -1:
            print(-1)
        else:
            print(stack_list[top])
