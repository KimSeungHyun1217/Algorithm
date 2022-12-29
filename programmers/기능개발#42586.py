from collections import deque
def solution(progresses, speeds):
    answer = []
    check = []
    
    while progresses:
        num = 0
        
        while progresses and progresses[0] >= 100:
            num += 1
            progresses.pop(0)
            speeds.pop(0)
            
        progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
        
        if num:
            answer.append(num)
    
    return answer