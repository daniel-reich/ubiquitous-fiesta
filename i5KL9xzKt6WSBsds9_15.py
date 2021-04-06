
def can_move(piece, current, target):
  #"Pawn", "Knight", "Bishop", "Rook", "Queen" and "King"
  if piece == "Knight":
    return is_knight(current, target)
  elif piece == "Rook":
    return radius_horizontal(current, target) > 0 or radius_vertical(current, target) > 0
  elif piece == "Queen":
    return radius_horizontal(current, target) > 0 or radius_vertical(current, target) > 0 or radius_diagonal(current,target) > 0
  elif piece == "King":
    return radius_horizontal(current, target) == 1 or radius_vertical(current, target) == 1 or radius_diagonal(current,target) ==1
  elif piece == "Bishop":
    return radius_diagonal(current, target) > 0
  elif piece == "Pawn":
    return (radius_vertical(current,target) == 2 and int(current[1]) == 2) or radius_vertical(current,target) == 1
def radius_horizontal(current, target):
  cols = {letter:(index+1) for index,letter in enumerate("ABCDEFGH")}
  return abs(int(cols[current[0]]) - int(cols[target[0]])) if current[1] == target[1] else 0
def radius_vertical(current, target):
  return abs(int(current[1]) - int(target[1])) if current[0] == target[0] else 0
def radius_diagonal(current, target):
  cols = {letter:(index+1) for index,letter in enumerate("ABCDEFGH")}
  rise = int(current[1])-int(target[1])
  run = cols[current[0]] - cols[target[0]]
  return abs(rise) if abs(rise) == abs(run) else 0
def is_knight(current, target):
  cols = {letter:(index+1) for index,letter in enumerate("ABCDEFGH")}
  rise = int(current[1])-int(target[1]) + 1
  run = cols[current[0]] - cols[target[0]] + 1
  if (rise == 3 and run == 2) or (rise == 2 and run == 3):
    return True
  return False

