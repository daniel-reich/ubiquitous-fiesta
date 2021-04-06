
def divide(x, y):
  if y<0: return divide(-x, -y)
  if x<0: return -divide(-x,y)
  return 0 if x<y else 1 + divide(x-y,y)

