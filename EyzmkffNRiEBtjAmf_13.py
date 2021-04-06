
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c,w,h):
  holeSize = w*h
  brickSizes = [a*b,b*c,a*c]
  for i in brickSizes:
    if i <= holeSize:
      return True
  return False

