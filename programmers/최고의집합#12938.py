def solution(n, s):
    if s<n: return [-1]
    
    start = s//n
    
    answer = [start for _ in range(n)]
    
    for i in range(s%n):
        answer[-i-1] += 1
        
    return answer