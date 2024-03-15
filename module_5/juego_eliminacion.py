jugadores = []
k = int(input())

while k > 0:
    if k in jugadores:
        jugadores.remove(k)
    elif (k + 1) in jugadores:
        jugadores.remove(k + 1)
    elif (k - 1) in jugadores:
        jugadores.remove(k - 1)
    else:
        jugadores.append(int(k))
    k = int(input())

print(' '.join(map(str, jugadores)) if jugadores else 0)