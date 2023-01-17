from collections import deque

def solution(priorities, location):
    stack = []
    check = len(priorities)
    d = [[i , item] for i,item in enumerate(priorities)]
    
    d = deque(d)
    m = max(d , key = lambda x : x[1])[1]
    
    while len(stack) != check:
        if d[0][1] < m:
            d.append(d.popleft())
        else:
            stack.append(d.popleft())
            if d:
                m = max(d , key = lambda x : x[1])[1]
    
    
    return stack.index([location,priorities[location]]) + 1