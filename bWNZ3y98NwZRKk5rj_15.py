
def block_player(a, b):
  straight = [[0,1,2],[3,4,5],[6,7,8]]
  inverse = [list(x) for x in zip(*straight)]
  diagonals = [[0,4,8],[2,4,6]]
  lst = straight+inverse+diagonals
  res = [x for x in lst if a in x and b in x][0]
  return [x for x in res if a!=x!=b][0]

