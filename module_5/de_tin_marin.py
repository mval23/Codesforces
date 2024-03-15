def tin_marin(l, k):
    p = (k - 1) % len(l)
    while len(l) > 1:
        k = (l.pop(p) % len(l))
        k = 1 if k == 0 else k
        p += (k - 1)
        p = (p % len(l)) if p >= len(l) else p
    return l[0]


c = int(input())

for _ in range(c):
    N, K = map(int, input().split(' '))
    L = [i for i in range(1, N + 1)]
    print(tin_marin(L, K))
