import sys

def binarycheck(arr,target):
    high = len(arr) -1
    low = 0

    while low<=high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return -1 


input = sys.stdin.readline

N = int(input())
card = list(map(int,input().split()))

M = int(input())
check = list(map(int,input().split()))

answer = []
card.sort()
for cc in check:
    if binarycheck(card,cc) >=0:
        answer.append('1')
    else:
        answer.append('0')


print(' '.join(answer))