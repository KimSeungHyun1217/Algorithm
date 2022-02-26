import sys

input = sys.stdin.readline

num = int(input())

queue_list = []

for _ in range(num):
    command = input().strip().split(" ")

    if command[0] == 'push':
        queue_list.append(command[1])

    elif command[0] == 'pop':
        if len(queue_list) ==0:
            print(-1)
        else:
            print(queue_list[0])
            del queue_list[0]

    elif command[0] == 'size':
        print(len(queue_list))

    elif command[0] == 'empty':
        if len(queue_list) == 0:
            print(1)
        else: print(0)

    elif command[0] == 'front':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[0])
    else:
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[len(queue_list)-1])

