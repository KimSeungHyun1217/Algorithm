import sys

input = sys.stdin.readline

num = int(input())

num_list = list(map(int,input().split()))
checkpoint = max(num_list)
flag = True
for i in range(num):
    if checkpoint == num_list[i]:
        print(-1, end=" ")
        if num-1 == i:
            flag = False
        continue
    for j in range(i+1,num):

        if num_list[i] < num_list[j]:
            print(num_list[j],end=" ")
            break
        if j == num -1:
            print(-1,end=" ")

if flag:
    print(-1)