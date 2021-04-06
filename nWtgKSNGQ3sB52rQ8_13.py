
def evenly_divisible(a, b, c):
  r=0
  for i in range(a,b+1):
    if i%c==0:
      r+=i
  return r

