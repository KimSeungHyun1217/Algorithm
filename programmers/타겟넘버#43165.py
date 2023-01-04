from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        check , i = queue.popleft()
        i += 1
        if i < n:
            queue.append([check + numbers[i],i])
            queue.append([check - numbers[i],i])
        else:
            if check == target:
                answer+= 1
        
    return answer