
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
  combs = [(a,b), (a,c), (b,c)]
  return any(comb <= (w,h) for comb in combs)

