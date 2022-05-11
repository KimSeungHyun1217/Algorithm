import sys
from collections import deque



def dfs(num):
    visit[num] = 1
    # print(num,end = " ")
    for i in range(1,n+1):
        if visit[i] == 0 and graph[num][i] == 1:
            dfs(i)

def bfs(num):
    q = deque()
    q.append(num)
    visit_bfs[num] = 1
    while q:
        x = q.popleft()
        print(x, end = " ")
        for i in range(1,n+1):
            if visit_bfs[i] == 0 and graph[x][i] == 1:
                q.append(i)
                visit_bfs[i] = 1


input = sys.stdin.readline

# n,m,v = map(int,input().split())
n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]
visit = [0] * (n+1)
visit_bfs = [0] * (n+1)
for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = graph[y][x] = 1

dfs(1)
print(sum(visit)-1)
# print("\n")
# bfs(v)