
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
  a,b,c = sorted([a,b,c])
  w,h = sorted([w,h])
  return (w>=a and h >= b) or (w>=b and h>=c)

