
def get_diagonals(lst):
  d1 = [lst[x][y] for x in range(len(lst)) for y in range(len(lst[x]))if y==x ]
  d2 = [lst[::-1][x][y] for x in range(len(lst)) for y in range(len(lst[x]))if y==x ]
  return  [d1, d2[::-1]]

