fan = tuple(input().split(' '))
l = []

while fan[0] != '0':
    if len(l) in l:
        l.remove(len(l))
    if int(fan[1]) > len(l):
        l.append(int(fan[1]))
    fan = tuple(input().split(' '))

print(len(l))