
def quartic_equation(a,b,c):
  disc = b**2 - 4*a*c
  if disc<0:
    return 0
  if disc>0:
    if c < 0:
      return 2
    elif c>0:
      if b<0:
        return 4
      if b>0:
        return 0
    else:
      if b<0:
        return 3
      else:
        return 1

