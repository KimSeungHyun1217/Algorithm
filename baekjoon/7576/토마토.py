from collections import deque

dx = [-1,1,0,0]  
dy = [0,0,-1,1]


w,h = map(int,input().split())
graph = []

for _ in range(h):
    graph.append(list(map(int,input().split())))

q = deque([])

for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            q.append([i,j])



while q:
    x,y = q.popleft()
    
    for i in range(4):
        ax = x+dx[i]
        ay = y+dy[i]

        if ax >= 0 and ax < h and ay >= 0 and ay<w:
            if  graph[ax][ay] == 0:
                graph[ax][ay] = graph[x][y] + 1
                q.append([ax,ay])
flag = True
ans = -3
for i in range(h):
    if not flag:
        break
    for j in range(w):
        if graph[i][j] == 0:
            print(-1)
            flag=False
            break
        else:
            if graph[i][j] > ans:
                ans = graph[i][j]
    

if flag:
    print(ans-1)

