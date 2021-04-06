
def onDiagonal(queens):
  l = 'ABCDEFGH'
  n = '12345678'
  n_delt = '87654321'
  a, b = l.index(queens[0][0]), n.index(queens[0][1])
  a1, b1 = l.index(queens[1][0]), n.index(queens[1][1])
  c, d = l.index(queens[0][0]), n_delt.index(queens[0][1])
  c1, d1 = l.index(queens[1][0]), n_delt.index(queens[1][1])
  if (a1-a) == (b1-b):
    return True
  elif (c1-c) == (d1-d):
    return True
  else:
    return False
​
def can_capture(queens):
  if queens[0][0] == queens[1][0]:
    return True
  if queens[0][1] == queens[1][1]:
    return True
  if onDiagonal(queens):
    return True
  else:
    return False

