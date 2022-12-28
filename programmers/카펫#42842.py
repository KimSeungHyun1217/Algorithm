def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer.append(3)
        answer.append(3)
    else:
        for h in range(1,yellow//2 + 1):
            if yellow % h == 0:
                w = yellow // h

                if (h*2) + (w*2) + 4 == brown:
                    answer.append(w+2)
                    answer.append(h+2)
                    break
    
    return answer