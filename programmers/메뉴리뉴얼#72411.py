from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order),c)
            
        counter = Counter(temp)
        
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(count) for count in counter if counter[count] == max(counter.values())]
    
    return sorted(answer)