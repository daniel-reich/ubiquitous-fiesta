
def legal_move(x, y):
    if not x and not y:
        return x, y
    elif x and not y:
        return x[:-1], [x[-1]]
    elif not x and y:
        return [y[-1]], y[:-1]
    elif x[-1] < y[-1]:
        return x[:-1], y + [x[-1]]
    elif x[-1] > y[-1]:
        return x + [y[-1]], y[:-1]
​
​
def tower_of_hanoi(disks, move):
    a, b, c = [i for i in range(disks, 0, -1)], [], []
    moves = 0
    if not disks % 2:
        while moves < move:
            a, b = legal_move(a, b)
            moves += 1
            if moves == move:
                return a, b, c
            a, c = legal_move(a, c)
            moves += 1
            if moves == move:
                return a, b, c
            b, c = legal_move(b, c)
            moves += 1
            if moves == move:
                return a, b, c
    else:
        while moves < move:
            a, c = legal_move(a, c)
            moves += 1
            if moves == move:
                return a, b, c
            a, b = legal_move(a, b)
            moves += 1
            if moves == move:
                return a, b, c
            b, c = legal_move(b, c)
            moves += 1
            if moves == move:
                return a, b, c
    return a, b, c

