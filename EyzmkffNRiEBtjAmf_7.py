
def does_brick_fit(a,b,c, *hole):
  brick = sorted([a, b, c])
  return brick[1] <= max(hole) and brick[0] <= min(hole)

