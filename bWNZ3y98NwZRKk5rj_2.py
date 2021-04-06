
def block_player(a, b):
  lines = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
  for i in lines:
    if a in i and b in i:
      return [c for c in i if c!=a and c!=b][0]

