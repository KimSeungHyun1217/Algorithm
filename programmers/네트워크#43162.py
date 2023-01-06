from collections import deque

def BFS(n,visited ,v ,computers):
    queue = deque([v])
    
    while queue:
        x = queue.popleft()
        visited[x] = True
        for i in range(n):
            if x!=i and computers[x][i] and visited[i] == False:
                queue.append(i)

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for v in range(n):
        if not visited[v]:
            BFS(n,visited,v,computers)
            answer += 1
    return answer