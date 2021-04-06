
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
  a1, b1, c1 = sorted([a,b,c])
  w1, h1 = sorted([w,h])
  
  return (a1 <= w1) and (b1 <= h1)

