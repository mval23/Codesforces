from collections import deque


def d(string, q, c, e):
    num = ""
    string += " ;"
    count = 0
    other = 0
    for i in (string):
        if i == ";":
            return c, e
        elif i != " ":
            num += i
        else:
            count += 1
            number = int(num) - 1
            if number == 0:
                if e == count:
                    return count + other, None
                c -= 1
                if e > count:
                    other += 1
                    e -= 1
                    count -= 1

            else:
                q.append(number)
            num = ""


def t(q, c, e, count):
    delta_pos = 0
    compare = 1
    deleted = 0
    while True:
        count += 1
        petitions = q.popleft() - 1

        if petitions == 0:
            deleted += 1
            if compare == e:
                return count * 5
            if compare < e:
                delta_pos += 1

        else:
            q.append(petitions)

        if compare == c:
            c -= deleted
            deleted = 0
            e -= delta_pos
            compare = 0
            delta_pos = 0

        compare += 1


output = ""
for _ in range(int(input())):
    info = tuple(map(int, input().split()))
    q = deque()

    c, e = d(input(), q, info[0], info[1])
    if e != None:
        output += f"{t(q, c, e, info[0])}\n"
    else:
        output += f"{c * 5}\n"

print(output[:-1])