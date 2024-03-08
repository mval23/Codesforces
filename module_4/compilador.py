from collections import deque

C = int(input())

for _ in range(C):
    A = deque()
    L = tuple(input().split()[:-1:])
    C = True

    for j in range(len(L)):
        if L[j] in ('{', '[', '('):
            A.append(L[j])
        else:
            if len(A) == 0:
                C = False
                break
            elif A[-1] + L[j] not in ('{}', '[]', '()'):
                C = False
                break
            else:
                A.pop()

    if C:
        print('correcta')
    else:
        print('incorrecta')

# opt 2

from collections import deque


def c(i):
    if i == ")":
        return 0
    if i == "]":
        return 1
    if i == "}":
        return 2
    else:
        return 3


def n(i):
    if i == "(":
        return 0
    if i == "[":
        return 1
    if i == "{":
        return 2
    else:
        return 3


def d(s):
    q = deque()
    num = ""

    norm = ("(", "[", "{")

    for i in s:
        comp = c(i)
        normal = n(i)

        if i == ";" and len(q) > 0:
            return "incorrecta"

        if comp != 3:
            if len(q) == 0:
                return "incorrecta"
            if q.pop() != norm[comp]:
                return "incorrecta"

        elif i != " " and i != ";":
            q.append(i)

    return "correcta"


out = ""
for _ in range(int(input())):
    out += f"{d(input())}\n"

print(out[:-1])
