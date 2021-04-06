
def does_brick_fit(a,b,c, w,h):
  vals = [a+b,a+c,b+c]
  return any(v <= w+h for v in vals)

