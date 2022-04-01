import sys

input = sys.stdin.readline

def gcd(a,b):
    if a%b == 0:
        return b
    return gcd(b,a%b)

N,S = map(int,input().split())

bro = list(map(int,input().split()))

for i in range(N):
    bro[i] = abs(bro[i] - S)

D = min(bro)
for i in bro:
    D = gcd(D,i)

print(D)
