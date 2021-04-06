
def split(x):
  p = 1
  for i in range(2,x):
    if (x/i)**i > p:
      p = (x/i)**i
  return round(p,1)

