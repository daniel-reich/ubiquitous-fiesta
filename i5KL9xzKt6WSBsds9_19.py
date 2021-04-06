
def can_move(piece, current, target):
    h_diff = ord(target[0]) - ord(current[0])
    v_diff = int(target[1]) - int(current[1])
    if piece == 'Pawn':
        return h_diff == 0 and (v_diff == 1
                                or (current[1] == '2' and v_diff == 2))
    elif piece == 'Knight':
        return ((abs(h_diff) == 2 and abs(v_diff) == 1)
                or (abs(h_diff) == 1 and abs(v_diff) == 2))
    elif piece == 'Bishop':
        return abs(h_diff) == abs(v_diff)
    elif piece == 'Rook':
        return h_diff == 0 or v_diff == 0
    elif piece == 'Queen':
        return h_diff == 0 or v_diff == 0 or (abs(h_diff) == abs(v_diff))
    elif piece == 'King':
        return ((h_diff == 0 and abs(v_diff) == 1)
                or (v_diff == 0 and abs(h_diff) == 1)
                or abs(h_diff) == abs(v_diff) == 1)

