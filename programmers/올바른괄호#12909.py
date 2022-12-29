def solution(s):
    
    check = []
    for i in s:
        if i == "(":
            check.append(i)
        else:
            if not check:
                return False
            else:
                check.pop()
    return not check