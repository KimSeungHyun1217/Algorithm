
from collections import deque
import sys

input = sys.stdin.readline

num = int(input())

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

def bfs(chess,start,end,l):
    q = deque()
    q.append(start)

    while q:
        x,y = q.popleft()
        if x == end[0] and y == end[1]:
            print(chess[x][y])
            break
        for i in range(8):
            if 0 <= x + dx[i] < l and 0<= y + dy[i] < l:
                if chess[x + dx[i]][y + dy[i]] == 0 :
                    chess[x + dx[i]][y + dy[i]] = chess[x][y] +1
                    q.append([x + dx[i],y + dy[i]])


for _ in range(num):
    l = int(input())
    chess = [[0] * l for _ in range(l)]
    start = list(map(int,input().split()) )
    end = list(map(int,input().split()))
    bfs(chess,start,end,l)





