from collections import deque

uroo = deque()
while True:
    m = input()

    if m[:6] == "agrega":
        uroo.append(int(m[7:]))

    if m == "engulle":
        if len(uroo) == 0:
            pass
        elif len(uroo) == 1:
            uroo.pop()
        elif len(uroo) > 1:
            head = uroo.popleft()
            tail = uroo.pop()
            if head > tail:
                uroo.appendleft(head)
            else:
                uroo.append(tail)

    if m == "termina":
        if len(uroo) == 0:
            print("uroboro vacio")
        if len(uroo) == 1:
            tail = uroo.pop()
            print(f"cabeza {tail} cola {tail}")
        if len(uroo) > 1:
            print(f"cabeza {uroo.popleft()} cola {uroo.pop()}")
        break