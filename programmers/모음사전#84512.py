from itertools import product

def solution(word):
    answer = []
    idx = 1
    dic = ['A','E','I','O','U']
    
    for i in range(1,6):
        for w in product(dic,repeat = i):
            answer.append(''.join(w))
                
    answer.sort()
        
    return answer.index(word) + 1