from collections import deque

def check(begin,word):
    dif = 0
    for i in range(len(begin)):
        if begin[i] != word[i]:
            dif += 1
            
    return True if dif == 1 else False

def BFS(wordidx , target , words):
    visited = [False] * len(words)
    
    queue = deque()
    queue.append([wordidx,1])
    while queue:
        idx, p = queue.popleft()
        
        visited[idx] = True
        if words[idx] == target:
            return p
        for i in range(len(words)):
            if i != idx and not visited[i] and check(words[idx] , words[i]):
                queue.append([i,p+1])
                
    return 0
        
        
def solution(begin, target, words):
    answer = []
    for word in words:
        if check(begin , word):
            an = BFS(words.index(word),target,words)
            if  an != 0:
                answer.append(an)
    
    
    
    return min(answer) if answer else 0
