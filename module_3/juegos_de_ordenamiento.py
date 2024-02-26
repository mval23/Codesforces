def cant_movs(arr):
    n = len(arr)
    cant = 0
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cant += 1
    return cant


N = int(input())
for _ in range(N):
    print(cant_movs(list(map(int, input().split()))))