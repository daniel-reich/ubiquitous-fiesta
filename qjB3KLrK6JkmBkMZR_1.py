
def can_capture(queens):
  same_row = bool(queens[0][0] == queens[1][0])
  same_col = bool(queens[0][1] == queens[1][1])
  diagonal = bool(abs(ord(queens[0][0])-ord(queens[1][0])) == abs(ord(queens[0][1])-ord(queens[1][1])))
  
  return same_row or same_col or diagonal

