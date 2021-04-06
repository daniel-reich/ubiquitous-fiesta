
def can_capture(queens):
  Row = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
  Q1R = queens[0][0]
  Q1C = queens[0][1]
  Q2R = queens[1][0]
  Q2C = queens[1][1]
  if Row[Q1R] == Row[Q2R] or int(Q1C) == int(Q2C):
    return True
  else:
    if abs(Row[Q1R]-Row[Q2R]) == abs(int(Q1C)-int(Q2C)):
      return True
    else:
      return False

