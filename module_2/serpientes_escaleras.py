C = int(input())

def play(M, board):
    ya = [False] * len(board)
    s = 0
    pos = 0

    while True:
        if pos < 0 or pos >= len(board) or ya[pos]:
            break
        ya[pos] = True
        pos += board[pos]
        s += 1
    return s


for _ in range(C):
    M = int(input())
    board = tuple(map(int, input().split()))
    print(play(M, board))