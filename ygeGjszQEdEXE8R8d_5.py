
def move(mat):
  s=lambda x,i:x[i:]+x[:i]
  if type(mat)==list: move.m=mat; return move
  if mat == "stop": return move.m
  move.m=[s(move.m,1),s(move.m,-1),[s(i,1) for i in move.m],[s(i,-1) for i 
    in move.m]][["up","down","left","right"].index(mat)]
  return move

