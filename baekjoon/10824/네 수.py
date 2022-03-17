import sys

input = sys.stdin.readline

num = list(map(int,input().split()))

print(int(str(num[0]) + str(num[1]))+int(str(num[2])+str(num[3])))