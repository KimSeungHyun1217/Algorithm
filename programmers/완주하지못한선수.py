def solution(participant, completion):
    answer = ""
    dictpart = {}
    for name in participant:
        if name not in dictpart:
            dictpart[name] = 1
        else:
            dictpart[name] += 1
    for name in completion:
        if not (dictpart[name] -1):
            dictpart.pop(name)
        else:
            dictpart[name] -= 1
    answer=  list(dictpart.keys())[0]
    return answer

def Best_solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]