C = int(input())

for _ in range(C):
    M, N = map(int, input().split())
    b = tuple(map(int, input().split()))
    g = [sum(b[i::M]) for i in range(M)]
    print(max(g) - min(g))




