
def get_pos(pos):
    return int(pos[1]), ord(pos[0]) - 64
​
def can_move(piece, current, target):
    row1, col1 = get_pos(current)
    row2, col2 = get_pos(target)
    row_diff, col_diff = abs(row1 - row2), abs(col1 - col2)
    if piece == "Pawn":
        return col_diff == 0 and (row_diff == 1 or \
                                  (row_diff == 2 and row1 == 2))
    elif piece == "Knight":
        return [row_diff, col_diff] in [[1, 2], [2, 1]]
    elif piece == "Bishop":
        return row_diff == col_diff
    elif piece == "Rook":
        return row_diff == 0 or col_diff == 0
    elif piece == "Queen":
        return row_diff == 0 or col_diff == 0 or row_diff == col_diff
    elif piece == "King":
        return [row_diff, col_diff] in [[0, 1], [1, 0], [1, 1]]
    assert False, "We should never reach this point, sucker!"

