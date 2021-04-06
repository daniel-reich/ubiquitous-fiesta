
def can_move(piece, current, target):
  ranks = "ABCDEFGH"
  rankdiff = abs(ranks.index(target[0]) - ranks.index(current[0]))
  filediff = abs(int(target[1]) - int(current[1]))
  if piece == "Pawn":
    if current[1] == "2":
      return 1 <= filediff <= 2 and rankdiff == 0
    else:
      return filediff == 1 and rankdiff == 0
  if piece == "Knight":
    return (rankdiff == 2 and filediff == 1) or (rankdiff == 1 and filediff == 2)
  if piece == "Bishop":
    return rankdiff == filediff
  if piece == "Rook":
    return rankdiff == 0 or filediff == 0
  if piece == "Queen":
    return rankdiff == filediff or (rankdiff == 0 or filediff == 0)
  if piece == "King":
    return rankdiff < 2 and filediff < 2

