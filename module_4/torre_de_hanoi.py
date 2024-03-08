from collections import deque

c = int(input())

for _ in range(c):
    d = int(input())
    a = deque([i for i in range(d, 0, -1)])
    b, c = deque(), deque()
    i = False

    while True:
        m = tuple(input().split())
        if m[0] == 'X':
            break
        elif not i:
            if m[0] == 'A':
                if a:
                    disk = a.pop()
                else:
                    disk = 0
                    i = True
            elif m[0] == 'B':
                if b:
                    disk = b.pop()
                else:
                    disk = 0
                    i = True
            else:
                if c:
                    disk = c.pop()
                else:
                    disk = 0
                    i = True

            if m[1] == 'A':
                if a:
                    if disk > a[-1]:
                        i = True
                    else:
                        a.append(disk)
                else:
                    a.append(disk)
            elif m[1] == 'B':
                if b:
                    if disk > b[-1]:
                        i = True
                    else:
                        b.append(disk)
                else:
                    b.append(disk)
            else:
                if c:
                    if disk > c[-1] and c:
                        i = True
                    else:
                        c.append(disk)
                else:
                    c.append(disk)

    if i:
        print('secuencia invalida')
    elif c == deque([i for i in range(d, 0, -1)]):
        print('soluciona la torre')
    else:
        print('no soluciona la torre')