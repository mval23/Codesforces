def dist_postes(postes, pairs):
    pos = {code: num for num, code in enumerate(sorted(postes))}
    for p1, p2 in pairs:
        print(abs(pos[p1] - pos[p2]), "kms")


_ = int(input())
postes = list(map(int, input().split()))
P = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(P)]
dist_postes(postes, pairs)