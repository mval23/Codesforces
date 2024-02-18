N = int(input())
p = tuple(map(int, input().split(","))) + tuple(map(int, input().split(","))) + tuple(map(int, input().split(",")))
X = 0
Y = 0
Z = 0

for i in range(N):
    s, l, i = p[i], p[i + N], p[i + 2 * N]
    g = sum((s, l, i)) % 2
    X += 1 if s % 2 == g else 0
    Y += 1 if l % 2 == g else 0
    Z += 1 if i % 2 == g else 0

print("SO:" + str(X) + ", LAR:" + str(Y) + ", IS:" + str(Z))
