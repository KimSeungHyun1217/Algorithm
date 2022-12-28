from itertools import permutations

def godun(k,dungeons,cost):
    ans = 0
    for c in cost:
        if dungeons[c][0] <= k:
            k -= dungeons[c][1]
            ans += 1
    return ans


def solution(k, dungeons):
    answer = -1
    dnum = len(dungeons)
    check = [i for i in range(dnum)]
    
    for i in permutations(check,dnum):
        x = godun(k,dungeons,i)
        if x > answer:
            answer = x
    
    
    
    return answer