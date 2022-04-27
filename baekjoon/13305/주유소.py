import sys

input = sys.stdin.readline

N = int(input())
use = list(map(int,input().split()))
charge = list(map(int,input().split()))

ans = use[0] * charge[0]
check = charge[0]                
for i in range(1,len(charge)-1): 
    if check > charge[i]:
        check = charge[i]
    ans += use[i] * check
    
print(ans)
    