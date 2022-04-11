import sys
input = sys.stdin.readline

num = int(input())
casenum = []
for _ in range(num):
    casenum.append(int(input()))

maxnum = max(casenum)
check = [True for i in range(maxnum + 1)]

for i in range(2, int(maxnum**0.5) + 1):
    if check[i]:
        for k in range(i + i, maxnum +1, i):
            check[k] = False

for case in casenum:
    result = 0
    
    for i in range(2, case//2 + 1):
        if check[i] and check[case - i]:
            result += 1

    print(result)