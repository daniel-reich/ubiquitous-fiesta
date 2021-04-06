
def can_move(piece, current, target):
  c = (ord(current[0])-64)*10 + int(current[1])
  t = (ord(target[0])-64)*10 + int(target[1])
  
  if piece == "Pawn":
    return t-c == 1
  elif piece == "Knight":
    return abs(t-c) in [8,12,19,21]
  elif piece == 'Bishop':
    return not abs(t-c)%11 or not abs(t-c)%9
  elif piece == 'Rook':
    return t//10 == c//10 or t%10 == c%10
  elif piece == 'Queen':
    return not abs(t-c)%11 or not abs(t-c)%9 or t//10 == c//10 or t%10 == c%10
  return abs(t//10 - c//10)<2 and abs(t%10 - c%10)<2

