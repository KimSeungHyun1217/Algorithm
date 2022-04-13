A,B = map(int,input().split())
num = int(input())
numlist = list(map(int,input().split()))

n = -1
x = 0

for i in range(num):
    x += (A**i) * numlist[n]
    n -= 1

numlist =[]

while x != 0:
    numlist.append(str(x%B))
    x //= B

numlist.reverse()

print(" ".join(numlist))