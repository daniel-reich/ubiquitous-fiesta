
def boxes(weights):
  b,x = 1,0
  for i in weights:
    if x+i>10: b,x = b+1,0
    x+=i
  return b

