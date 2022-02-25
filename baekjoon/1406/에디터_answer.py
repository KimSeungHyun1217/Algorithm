import sys

input = sys.stdin.readline

sentence = list(input().strip())


num = int(input())
cursor = len(sentence)
stack_list=[]   #커서가 왼쪽으로 움직일때마다 append 해주는 list

for i in range(num):
    command = input().strip()
    command = command.split(" ")
    if command[0] == 'L' and len(sentence) != 0: #커서가 왼쪽으로 움직일때 sentence가 0이면 동작 하지 않도록 설정
        stack_list.append(sentence.pop())
    if command[0] == 'D' and len(stack_list) != 0: #커서가 오른쪽으로 움직일때 stack_list가 0이면 동작하지 않도록 설정
        sentence.append(stack_list.pop())
    if command[0] == 'B' and len(sentence) != 0: #sentence가 비어있으면 동작 x
        sentence.pop()
    if command[0] == 'P':
        sentence.append(command[1])

for i in range(len(stack_list)):
    sentence.append(stack_list.pop())   #stack이기 때문에 역순으로 저장 stack_list[::-1]로도 extend하여 for문 없이 설정 가능
for i in sentence:
   print(i,end="")