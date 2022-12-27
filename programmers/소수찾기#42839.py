from itertools import permutations

def prime_number(number):
    num = int(number)
    for f in range(2, int(num**0.5)+1):  
        if num % f == 0:     
            return False   
    return True

def solution(numbers):
    
    number = list(numbers)
    check = []
    answer = 0
    
    for i in range(1,len(number) + 1):
        for perm in permutations(number,i):
            check.append(int(''.join(perm)))
    check = list(set(check))        
    
    for i in check:
        if i != 0 and i != 1:
            if prime_number(i):
                answer += 1
    
    return answer