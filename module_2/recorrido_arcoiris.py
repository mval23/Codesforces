N = int(input())
p = tuple(map(str, input().split(", ")))


def arcoiris(p, N):
    l = []
    for i in range(N // 2):
        l.extend([p[i], p[-(i + 1)]])
    if N % 2 == 1:
        l.append(p[-(N // 2 + 1)])
    return ''.join(l)


print(arcoiris(p, N))


# opt 2
N = int(input())
p = tuple(map(str, input().split(", ")))

l = []
for i in range(N // 2):
    l.extend([p[i], p[-(i + 1)]])
if N % 2 == 1:
    l.append(p[-(N // 2 + 1)])


print(''.join(l))