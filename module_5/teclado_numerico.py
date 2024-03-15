n = []
commands = tuple(input().split())

while commands[0] != 'end':
    if commands[0] == 'end':
        break
    if commands[0] == 'C':
        if len(n) >= 1:
            n.pop()
    elif commands[0] == 'D':
        if int(commands[1]) <= len(n):
            n = n[:-int(commands[1])]
    elif commands[0] == 'M':
        if int(commands[2]) <= len(n):
            print("".join(n[int(commands[1]) - 1:int(commands[2])]))
    else:
        n.append(commands[0])
    commands = tuple(input().split())