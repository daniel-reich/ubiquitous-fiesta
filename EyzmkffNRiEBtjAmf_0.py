
def does_brick_fit(a,b,c,w,h):
  x,y= sorted([a,b,c]),sorted([w,h])
  return x[0]<=y[0] and x[1]<=y[1]

