N = int(input())
t = tuple(map(int, input().split()))
for i in range(N-2, -1, -1):
    print(sum(t[i:]))