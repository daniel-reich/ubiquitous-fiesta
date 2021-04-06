
def boxes(weights):
  s=0
  c=1
  for x in weights:
    if s+x<=10:
      s+=x
    else:
      c+=1
      s=0
      s+=x
  return c

