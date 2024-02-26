
_ = int(input())
vals = list(map(int, input().split(' ')))
N = int(input())
M = tuple(map(int, input().split(' ')))

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


for i in M:
    N += binary_search(vals, i)

print(N)
