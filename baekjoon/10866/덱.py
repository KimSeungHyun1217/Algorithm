import sys
from collections import deque

input =sys.stdin.readline

num = int(input())
de = deque([])
for _ in range(num):
    command = input().strip().split(" ")

    if command[0] == 'push_back':
        de.append(command[1])
    elif command[0] == 'push_front':
        de.appendleft(command[1])
    elif command[0] == 'pop_front':
        if de.__len__() == 0 :
            print(-1)
            continue
        print(de.popleft())
    elif command[0] == 'pop_back':
        if de.__len__() == 0 :
            print(-1)
            continue
        print(de.pop())
    elif command[0] == 'size':
        print(de.__len__())
    elif command[0] == 'empty':
        if de.__len__() == 0:
            print(1)
        else: print(0)
    elif command[0] == 'front':
        if de.__len__() == 0:
            print(-1)
        else:
            print(de[0])
    elif command[0] == 'back':
        if de.__len__() == 0:
            print(-1)
        else:
            print(de[de.__len__()-1])
