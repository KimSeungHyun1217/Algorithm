from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    x = Counter(tangerine)
    x = sorted(x.items(),key = lambda item: item[1],reverse = True)
    
    
    for _,i in x:
        k -= i
        answer += 1
        if k <=0:
            break
            
    return answer