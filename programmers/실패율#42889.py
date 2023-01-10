def solution(N, stages):
    answer = []
    term = []
    for i in range(1,N+1):
        if len(stages) == 0:
            term = [j for j in range(i,N+1)]     
            break
        check =[]
        fail = 0 
        for num in stages:
            if num <= i:
                fail += 1
            else:
                check.append(num)
        answer.append([i,fail / len(stages)])
        stages = check
    
    answer.sort(key = lambda k : k[1],reverse=True)
    answer = [i[0] for i in answer]
    answer.extend(term)
    return answer