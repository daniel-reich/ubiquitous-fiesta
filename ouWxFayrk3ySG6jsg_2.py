
def whoWon(b):
  cols = [list(i) for i in zip(*b)]
  dia1 = [[b[0][0], b[1][1], b[2][2]]]
  dia2 = [[b[2][0], b[1][1], b[0][2]]]
  for i in b + cols + dia1 + dia2:
    if set(i) == {'X'}:
      return 'X'
  return 'O'

