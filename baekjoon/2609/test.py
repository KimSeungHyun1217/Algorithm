import sys

input = sys.stdin.readline

a,b = map(int,input().split())

dae=0
flag = False
for i in range(1,b+1):
    if a%i ==0 and b%i ==0:
        dae = i

print(dae)
print(int(dae *(a/dae)*(b/dae)))
