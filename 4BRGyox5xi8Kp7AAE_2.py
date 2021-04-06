
def chess_board(p):
  l, n = list(p)
  return 'black' if ord(l) % 2 == int(n) % 2 else 'white'

