
def block_player(a, b):
  lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,5,7]]
  for l in lines:
    if a in l and b in l:
      for p in l:
        if p not in [a,b]:
          return p

