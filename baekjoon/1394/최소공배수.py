import sys

def gcd(a,b): #유클리드 호제법
    if a%b == 0:
        return b
    return gcd(b,a%b)



input = sys.stdin.readline

num = int(input())



for _ in range(num):
    a,b = map(int,input().split())
    x = gcd(a,b)
    print(int((a/x)*(b/x)*x))
