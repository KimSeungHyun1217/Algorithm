import sys
from itertools import combinations

def gcd(a,b): #유클리드 호제법
    if a%b == 0:
        return b
    return gcd(b,a%b)

num = int(input())

for _ in range(num):
    x = list(map(int,input().split()))[1:]
    gcdnum = 0

    gcdlist = list(combinations(x,2))

    for j in gcdlist:
        gcdnum += gcd(j[0],j[1])
    print(gcdnum)




