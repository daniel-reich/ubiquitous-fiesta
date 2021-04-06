
def shift_to_right(x, y):
  if y == 0:
    if int(x) != x:
      xt = str(x).split('.')
      if int(xt[1][0]) >= 5:
        if x >= 0:
          x = int(x)
        else:
          x = int(x) - 1
      else:
        x = int(x)
    return x
  else:
    return shift_to_right(x/2, y-1)

