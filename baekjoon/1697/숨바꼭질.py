
from collections import deque
import sys

input = sys.stdin.readline

N,K = map(int,input().split())
graph = [0] * 100001


q = deque()
q.append(N)


while q:
    z = q.popleft()
    if z == K:
        print(graph[z])
        break
    for ax in [z+1,z-1,z*2]:
        if 0 <= ax <= 100001:
            if graph[ax] == 0 :
                graph[ax] = graph[z] +1
                q.append(ax)




