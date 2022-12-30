#ABCDEFGHIJKLMNOPQRXTUVWXYZ
def solution(name):
    answer = 0
    
    check = len(name) - 1
    
    
    for i,a in enumerate(name):
        answer += min(ord(a) - ord('A') , ord('Z') - ord(a) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        check = min([check, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    answer += check
    return answer