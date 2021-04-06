
# (a,b,c) -- dimensions of the brick
# (w,h) -- dimensions of the hole
def does_brick_fit(a,b,c, w,h):
  if a * b <= w * h or a * c <= w * h or c * b <= w * h:
    return True
  else:
    return False

