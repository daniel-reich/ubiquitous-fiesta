
def can_move(piece, current, target):
    x = (ord(target[0]) - 64) - (ord(current[0]) - 64)
    y = int(target[1]) - int(current[1])
​
    if piece == 'Pawn':
        return (x, y) == (0, 1)
    if piece == 'Knight':
        return sorted((x, y)) in ([-2, -1], [-2, 1], [-1, 2], [1, 2])
    if piece == 'Bishop':
        return abs(x) == abs(y)
    if piece == 'Rook':
        return x == 0 or y == 0
    if piece == 'Queen':
        return abs(x) == abs(y) or (x == 0 or y == 0)
    if piece == 'King':
        return sorted((abs(x), abs(y))) in ([0, 1], [1, 1])

