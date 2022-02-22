a,b = map(int,input().split())
arr = list(map(int,input().split()))
sum = []

for i in range(a-2):
    for j in range(i+1,a-1):
        for k in range(j+1,a):
            sum.append(arr[i]+arr[j]+arr[k])
total =[]
for i in range(int((a*(a-1)*(a-2))/6)):
    if sum[i] >b:
        total.append(b)
    else:
        total.append(b-sum[i])
print(sum[total.index(min(total))])
