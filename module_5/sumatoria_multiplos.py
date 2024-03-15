# def sum_m(l, n):
#     return sum([i for i in l if i % n == 0])
#
#
# i = input().split(' ')
# l = []
#
# while i[0] != 'E':
#     if i[0] == 'A':
#         l.append(int(i[1])),
#     else:
#         print(sum_m(l, int(i[1])))
#     i = input().split()

# Option 2


i = input().split(' ')
l = []

while i[0] != 'E':
    if i[0] == 'A':
        l.append(int(i[1])),
    else:
        print(sum([n for n in l if n % int(i[1]) == 0]))
    i = input().split()