from collections import deque

def dFromString(s, q):
    n = ""
    for i in s:
        if i != " ":
            n += i
        else:
            q.append(int(n))
            n = ""
    q.append(int(n))

out = ""
for _ in range(int(input())):
    q = deque()
    dFromString(input(), q)

    while True:
        if len(q) < 2:
            out += f"1 {q.pop()}\n"
            break

        first, second = q.pop(), q.pop()

        if (first + second) % 2 == 0:
            q.append((first + second) // 2)
        else:
            out += f"{len(q) + 2} {first}\n"
            break

print(out[:-1])