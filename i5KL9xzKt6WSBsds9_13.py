
def can_move(piece, current, target):
    pawn1 = current[0] == target[0] and int(target[1]) == int(current[1]) + 1
    pawn2 = current[0] == target[0] == 'G' and int(target[1]) == int(current[1]) + 2
    knight1 = abs(int(target[1]) - int(current[1])) == 2 and abs(ord(target[0]) - ord(current[0])) == 1
    knight2 = abs(int(target[1]) - int(current[1])) == 1 and abs(ord(target[0]) - ord(current[0])) == 2
    rook = current[0] == target[0] or int(target[1]) == int(current[1])
    bishop = ord(target[0]) == ord(current[0]) + abs(int(target[1]) - int(current[1]))
    king = abs(int(target[1]) - int(current[1])) <= 1 and abs(ord(target[0]) - ord(current[0])) <= 1
   
    if piece == "Pawn":
        return pawn1 or pawn2
    if piece == "Knight":
        return knight1 or knight2
    elif piece == "Rook":
        return rook
    elif piece == "Bishop":
        return bishop
    elif piece == "King":
        return king
    elif piece == "Queen":
        return rook or bishop

