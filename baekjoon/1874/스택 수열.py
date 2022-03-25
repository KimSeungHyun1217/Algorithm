import sys

input = sys.stdin.readline

maxnum = int(input()) #max 값을 받음
flag= False
top = 0
stack_list = []
answer_list = []

for i in range(maxnum):
    num = int(input())
    if num > top:
        for i in range(top+1,num+1):  #입력 받은 값이 top보다 높을 경우
            stack_list.append(i)      #필요한 만큼 값을 더 추가
            answer_list.append("+")
        answer_list.append("-")       #마지막 값만 빼감
        stack_list.pop()
        top = num
    else:                             #입력 받은 값이 top보다 낮을 경우
        while(True):
            if len(stack_list) == 0:  #stack이 비어있으면 NO만 저장
                answer_list=[]
                answer_list.append("NO")
                flag = True
                break
            x = stack_list.pop()       #입력받은 값까지 pop해줌
            answer_list.append("-")
            if x == num:
                break
    if flag:
        break
for i in answer_list:
    print(i)