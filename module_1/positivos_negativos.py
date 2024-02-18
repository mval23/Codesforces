N = int(input())
L = []

for i in range(N):
    L.append(int(input()))


print("positivos {}, negativos {}".format(sum([n for n in L if n >0]), sum([n for n in L if n<0 ])))
