
def football(score):
  def r(t,j):
    if t==score:
      return 1
    elif t<score:
      c = 0
      x = [2, 3, 6, 7, 8]
      for i in range(j,5):
        c+=r(t+x[i],i)
      return c
    else:
      return 0
  return r(0,0)

