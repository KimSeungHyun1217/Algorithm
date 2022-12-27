def solution(answers):
    answer = []
    student = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    check = [0,0,0]
    for i,ans in enumerate(answers):
        for idx in range(3):
            if student[idx][i % len(student[idx])] == ans:
                check[idx] += 1
    print(check)
    ans = max(check)
    for i in range(3):
        if check[i] == ans:
            answer.append(i+1)
    answer = [i+1 for i in range(3) if check[i] == ans]
    answer.sort()
    return answer