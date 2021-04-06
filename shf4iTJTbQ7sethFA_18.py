
def magic_square_game(alice, bob):
  row, a = alice
  col, b = bob
  return  (a[col-1], a.count('1')%2, b.count('1')%2) == (b[row-1], 1, 0)

