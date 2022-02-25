import sys

input = sys.stdin.readline

sentence = list(input().strip())


num = int(input())
cursor = len(sentence)

for i in range(num):
    command = input().strip()
    command = command.split()
    if command[0] == 'L':
        if cursor == 0:
            continue
        cursor -= 1
    elif command[0] == 'D':
        if cursor == len(sentence):
            continue
        cursor += 1
    elif command[0] == 'B':
        if cursor == 0:
            continue
        del sentence[cursor-1]
        cursor -= 1
    else:
        sentence.insert(cursor,command[1])
        cursor += 1


for i in sentence:
    print(i,end="")