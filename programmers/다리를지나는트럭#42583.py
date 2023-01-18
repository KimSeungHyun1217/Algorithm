from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([truck_weights[0]])
    t = deque([0])
    i = 1

    check = len(truck_weights) -1
    while bridge:
        t = deque(map(lambda x:x+1 ,t))
        answer += 1
        if t[0] > bridge_length:
            t.popleft()
            bridge.popleft()
        if i <= check:
            if sum(bridge) + truck_weights[i] <= weight:
                bridge.append(truck_weights[i])
                t.append(1)
                i += 1
        
    return answer


print(solution(2,10,[7,4,5,6]))