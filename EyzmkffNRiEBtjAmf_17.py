
def does_brick_fit(a,b,c, w,h):
  a, b, c = sorted((a, b, c))
  return a*b <= w*h

