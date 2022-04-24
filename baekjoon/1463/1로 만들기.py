num = int(input())

d = [0] * (num + 1) # index num+1까지 0으로 설정 bottom up 방식


for i in range(2,num+1):
    d[i] = d[i-1] +1  # 1을 먼저 뺏을 경우로 설정
    if i%2 ==0:
        d[i] = min(d[i],d[i//2]+1)  # 1을 뺏을 때 vs 2로 나눴을때 더 작은 경우의 수로 설정
                                    # 1을 더해준 이유는 2로 나눴을 때의 경우의 수에서 1을 더한것(2로 나눠서)
    if i%3 ==0:                     
        d[i] = min(d[i],d[i//3]+1)  # 방법은 상동
                                    # 3으로 나눈게 더 크기 때문에 밑에 위치

print(d[num])