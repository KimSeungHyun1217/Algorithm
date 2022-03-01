import sys

input = sys.stdin.readline
num,kill = map(int , input().split())

queue_list = list(range(1,num+1))
kill_list = []

for _ in range(num):

    if len(queue_list) < kill:
        for _ in range(kill-1):
            queue_list.append(queue_list.popleft())
        kill_list.append(queue_list.popleft())
    else:
        queue_list.extend(queue_list[:kill-1])
        del queue_list[:kill-1]
        kill_list.append(queue_list.popleft())

