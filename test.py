
from collections import deque
import sys

input = sys.stdin.readline




# N,M = map(int,input().split())

# ladder = {}
# snake = {}
# for _ in range(N):
#     a,b = map(int,input().split())
#     ladder[a] = b
# for _ in range(M):
#     a,b = map(int,input().split())
#     snake[a] = b

# graph = [0] * 101
# n = len(graph)


# q = deque([1])
# x = []

# while q:
#     x = q.popleft()

#     if x == 100:
#         print(graph[100])
#         break

#     for i in range(1,7):
#         y = x+i
#         if y <= 100 and graph[y] ==0:
#             if y in ladder.keys():
#                 y = ladder[y]
#             if y in snake.keys():
#                 y = snake[y]
#             if graph[y] ==0:
#                 graph[y] = graph[x] + 1
#                 q.append(y)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

graph = []
N,M = map(int,input().split())

for i in range(N):
    graph.append(list(map(int,input().strip())))

q = deque([])
q.append([0,0])

while q:
    x,y = q.popleft()

    if x == N - 1  and y == M-1:
        print(graph[x][y] + 1)
        break
    
    if (graph[x+1][y] ==1 or x+1 == N) and (graph[x-1][y] ==1 or x-1 == -1) and (graph[x][y+1] == 1 or y+1 == M) and (graph[x][y-1] ==1 or y-1 == -1):
        

    for i in range(4):
        ax,ay = x+dx[i] ,y+dy[i]

        

        if 0<=ax<N and 0<=ay<M and graph[ax][ay] == 0:
            graph[ax][ay] = graph[x][y] + 1
            q.append(ax,ay)
    