import sys
from collections import deque

input = sys.stdin.readline

num,kill = map(int , input().split())

queue_list = deque(list(range(1,num+1)))
kill_list = deque([])

for _ in range(num):
    for _ in range(kill-1):
        queue_list.append(queue_list.popleft())  #큐에서 꺼내고 다시 넣어 kill 번째 수를 kill_list에 넘김
    kill_list.append(queue_list.popleft())

kill_list = list(map(str,kill_list))
print("<"+", ".join(kill_list)+">")
