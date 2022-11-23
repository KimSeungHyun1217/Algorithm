import sys

input = sys.stdin.readline

N,M = map(int,input().split())
S = []
for _ in range(N):
    S.append(input().strip())

check = []
for _ in range(M):
    check.append(input().strip())

def binarysearch(arr,target):
    high = len(arr) - 1
    low = 0

    while low<=high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
S.sort()

answer = 0
for word in check:
    if binarysearch(S,word) >=0:
        answer += 1

print(answer)