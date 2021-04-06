
def x_and_o(board):
  rows = [row.split('|') for row in board]
  cols = list(zip(*rows))
  diag1 = [[rows[0][0], rows[1][1], rows[2][2]]]
  diag2 = [[rows[2][0], rows[1][1], rows[0][2]]]
  combs = rows + cols + diag1 + diag2
​
  for i in range(len(combs)):
    if combs[i].count('X') == 2 and combs[i].count(' ') == 1:
      j = combs[i].index(' ')+1
      if combs[i] in rows:
        return [(i%3)+1, j]
      elif combs[i] in cols:
        return [j, (i%3)+1]
      elif combs[i] in diag1:
        return [j, j]
      elif combs[i] in diag2:
        return [4-j, j]
  return False

