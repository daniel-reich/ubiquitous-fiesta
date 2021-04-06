
def make_dartboard(n):
  s = [min(i + 1, n - i) for i in range(n)]
  board = [[min(rowMax, s[i]) for i in range(n)] for rowMax in s]
  board = [int("".join(str(x) for x in row)) for row in board]
  return board

