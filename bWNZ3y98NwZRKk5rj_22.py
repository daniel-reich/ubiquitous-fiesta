
def block_player(a, b):
  board = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
  ]
  ax, ay = int(a/3), a%3
  bx, by = int(b/3), b%3
  return board[(3-ax-bx)%3][(3-ay-by)%3]

