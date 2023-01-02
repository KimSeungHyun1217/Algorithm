def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i,cit in enumerate(citations):
        if i >= cit:
            return i
    return len(citations)