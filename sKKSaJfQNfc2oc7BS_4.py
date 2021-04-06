
def sle(m):
  for x in range(-2,4):
    for y in range(-2,3):
      if m[0][0]*x+m[0][1]*y==m[0][2] and m[1][0]*x+m[1][1]*y==m[1][2]:
        return (x,y)
  return False

