from collections import deque

d = tuple(map(int, input().split()))

n = d[0]
b = d[1]
t = 0
i = True

q = deque()

while True:
    t += 1

    if len(q) == 0 and i is not True:
        print("quedaron boletas disponibles")
        break

    if i is True:
        c = tuple(map(int, input().split()))
        b -= c[1]
        if t % 5 != 0:
            q.append(c)
    else:
        temp = q.popleft()
        if temp[1] >= b:
            print(temp[0], b)
            break
        else:
            b -= temp[1]

        if t % 5 != 0:
            q.append(temp)

    if t == n:
        i = False