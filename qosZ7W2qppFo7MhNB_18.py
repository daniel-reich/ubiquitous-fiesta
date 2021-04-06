
def hex_distance(grid):
  nL = 2*(grid[0].count("o") + grid[0].count("x")) -1
  
  pos = []
  sameLine = False
  for i in range(nL):
    aux = grid[i].split("x")
    Yshift = 0.5*abs(((nL+1)/2-1) -i)
    if len(aux) == 3:
      sameLine = True
      pos = pos + [[i, aux[0].count("o") + Yshift]]
      pos = pos + [[i, aux[0].count("o") + 1 + aux[1].count("o") + Yshift]]
    elif len(aux) == 2:
      pos = pos + [[i, aux[0].count("o") + Yshift]]
  deltaX2 = abs(pos[1][1]*2 - pos[0][1]*2)//1
  deltaY = abs(pos[1][0] - pos[0][0])
  if sameLine:
    return deltaX2//2
  elif deltaX2 <= deltaY:
    return deltaY
  else:
    return deltaY + (deltaX2-deltaY)//2

