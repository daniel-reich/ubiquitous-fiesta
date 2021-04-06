
def block_player(a, b):
  i = [[0,1,2],[3,4,5],[6,7,8]]
  for x in range(9):
    y = sorted([x,a,b])
    if (y[2]-y[1]) == (y[1]-y[0]):
      if (y[1]-y[0]) == 2:
        if y[1] != 4:
          pass
        else:
          return x
      else: 
        return x
    else:
      pass

