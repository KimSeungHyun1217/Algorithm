
from collections import deque
import sys

input = sys.stdin.readline


dx = [0,0,0,0,1,-1]  
dy = [0,0,-1,1,0,0]
dh = [1,-1,0,0,0,0]



w,h , a = map(int,input().split())
graph = []
for _ in range(a):
    x= []
    for _ in range(h):
        x.append(list(map(int,input().split())))
    graph.append(x)

q = deque([])

for k in range(a):
    for i in range(h):
        for j in range(w):
            if graph[k][i][j] == 1:
                q.append([k,i,j])



while q:
    z,x,y = q.popleft()
    
    for i in range(6):
        ax = x+dx[i]
        ay = y+dy[i]   
        az = z+dh[i]
        if ax >= 0 and ax < h and ay >= 0 and ay<w and az >= 0 and az < a:
            if  graph[az][ax][ay] == 0:
                graph[az][ax][ay] = graph[z][x][y] + 1
                q.append([az,ax,ay])
ans = -3
for i in range(h):
    for j in range(w):
        for k in range(a):
            if graph[k][i][j] == 0:
                print(-1)
                exit(0)
            else:
                if graph[k][i][j] > ans:
                    ans = graph[k][i][j]

print(ans-1)


