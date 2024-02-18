C = int(input())


def decrypt(M):
    new_M = []
    for i in range(len(M)//2):
        new_M.extend([M[2*i+1], M[i*2]])
    if len(M) % 2 == 1:
        new_M.append(M[-1])
    return ''.join(new_M)


for i in range(C):
    M = input().split()
    print(decrypt(M[::-1]))


# opt 2 was slower

C = int(input())

for _ in range(C):
    M = input().split()
    M =M[::-1]
    new_M = []
    for i in range(len(M) // 2):
        new_M.extend([M[2 * i + 1], M[i * 2]])
    if len(M) % 2 == 1:
        new_M.append(M[-1])
    print(''.join(new_M))

