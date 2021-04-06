
def can_move(piece, current, target):
  if current == target:
    return False
  elif piece == "Rook":
    for i in range(len(current)):
      if current[i] == target[i]:
        return True
    return False
  elif piece == "Pawn":
    if current[0] == target[0] and current[1] == "2" and target[1] == "4":
      return True
    elif current[0] == target[0] and int(current[1])+1 == int(target[1]):
      return True
    else:
      return False
  elif piece == "King":
    if abs(int(target[1]) - int(current[1])) < 2 and abs(ord(target[0]) - ord(current[0])) < 2:
      return True
    else:
      return False
  elif piece == "Bishop":
    if abs(int(target[1]) - int(current[1])) == abs(ord(target[0]) - ord(current[0])):
      return True
    else:
      return False
  elif piece == "Queen":
    if can_move("Rook", current, target) or can_move("Bishop", current, target):
      return True
    else:
      return False
  else:
    if abs(int(target[1]) - int(current[1])) == 2 and abs(ord(target[0]) - ord(current[0])) == 1:
      return True
    elif abs(int(target[1]) - int(current[1])) == 1 and abs(ord(target[0]) - ord(current[0])) == 2:
      return True
    else:
      return False

