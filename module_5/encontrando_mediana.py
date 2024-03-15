M = int(input())
l = []
n = int(input())

while n > 0:
    l.append(n)
    if len(l) % M == 0:
        l.sort()
        if len(l) % 2 == 0:
            n = len(l) // 2
            s = l[n - 1] + l[n]
            if s % 2 == 0:
                print(s // 2)
            else:
                print(str(s) + "/2")
        else:
            print(l[len(l) // 2])
    n = int(input())