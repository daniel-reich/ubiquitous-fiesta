
def can_move(piece, current, target):
    if piece == "Pawn":
        if current[0] == target[0] and ((abs(int(current[1]) - int(target[1])) == 1) or
                                            ((target[1] == "4" and current[1] == "2") or
                                                 (target[1] == "5" and current[1] == "7"))):
            return True
        else:
            return False
​
    elif piece == "Rook":
        if current[0] == target[0] or current[1] == target[1]:
            return True
        else:
            return False
    elif piece == "Bishop":
        if abs(ord(current[0]) - ord(target[0])) == abs(int(current[1]) - int(target[1])):
            return True
        else:
            return False
    elif piece == "Queen":
        if can_move("Rook", current, target) or can_move("Bishop", current, target):
            return True
        else:
            return False
    elif piece == "King":
        if (abs(ord(current[0]) - ord(target[0])) == abs(int(current[1]) - int(target[1])) == 1)\
                or (current[0] == target[0] and abs(int(current[1]) - int(target[1])) == 1) \
                or (current[1] == target[1] and abs(ord(current[0]) - ord(target[0])) == 1):
            return True
        else:
            return False
    elif piece == "Knight":
        if (abs(ord(current[0]) - ord(target[0])) == 1 and abs(int(current[1]) - int(target[1])) == 2) \
                or (abs(ord(current[0]) - ord(target[0])) == 2 and abs(int(current[1]) - int(target[1])) == 1):
            return True
        else:
            return False

