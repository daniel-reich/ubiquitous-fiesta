
def can_move(piece, current, target):
  destruct = lambda square: (ord(square[0]) - ord('A'), int(square[1])-1)
  x0, y0 = destruct(current)
  x1, y1 = destruct(target)
  dx, dy = x1 - x0, y1 - y0 
  if piece == "King":
    return (dx == 0 and abs(dy) == 1) or (dy == 0 and abs(dx) == 1) \
      or (abs(dx) == abs(dy) == 1)
  if piece == "Queen":
    return (dx == 0 and abs(dy) >= 1) or (dy == 0 and abs(dx) >= 1) \
      or (abs(dx) == abs(dy) >= 1)
  if piece == "Bishop":
    return (abs(dx) == abs(dy) >= 1)
  if piece == "Knight":
    return (abs(dx) == 2 and abs(dy) == 1) or (abs(dx) == 1 and abs(dy) == 2)
  if piece == "Rook":
    return (dx == 0 and abs(dy) >= 1) or (dy == 0 and abs(dx) >= 1)
  return dx == 0 and (dy == 1 or (y0 == 1 and dy == 2))

