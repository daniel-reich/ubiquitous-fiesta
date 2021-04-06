
def get_move(move):
    row, col = 8-int(move[1]), ord(move[0])-65
    return row, col
def can_move(piece, current, target):
    row, col = get_move(current)
    rowx, colx = get_move(target)
    if piece == 'Pawn':
        if (abs(row - rowx) == 1 or (row == 6 or row == 1 and abs(rowx-row) == 2)) and not abs(col-colx):
            return True
    if piece == 'Knight':
        if (abs(row - rowx) == 2 and abs(col-colx) == 1) or (abs(row-rowx)==1 and abs(col-colx)==2):
            return True
    if piece == 'Bishop':
        if abs(row-rowx) == abs(col-colx):
            return True
    if piece == 'Rook':
        if row - rowx and not col - colx or (col - colx and not row - rowx):
            return True
    if piece == 'Queen':
        if abs(row-rowx) == abs(col-colx) or (row - rowx and not col - colx or (col - colx and not row - rowx)):
            return True
    if piece == 'King':
        if abs(row-rowx) <= 1 and abs(col-colx) <= 1:
            return True
    return False

