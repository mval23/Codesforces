def find_div(p, conj):
    for i in range(1, p + 1):
        if p % i == 0 and i not in conj:
            return "No es PrimiConjunto"
    return "Es PrimiConjunto"


C = int(input())

for _ in range(C):
    N, P = map(int, input().split(' '))
    print(find_div(P, set(map(int, input().split(' ')))))