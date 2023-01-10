def solution(N, number):
    if number == 1:
        return 1
    answer = 0
    set_list = []
    
    for n in range(1,9):
        check = set()
        check.add(int(str(N)*n))
        
        for i in range(n-1):
            for op1 in set_list[i]:
                for op2 in set_list[-i-1]:
                    check.add(op1+op2)
                    check.add(op1-op2)
                    check.add(op1*op2)
                    if op2 !=0:
                        check.add(op1/op2)
                        
        if number in check:
            return n
        set_list.append(check)
    return -1