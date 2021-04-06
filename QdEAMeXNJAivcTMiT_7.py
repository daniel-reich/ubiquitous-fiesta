
def boxes(weights):
  t,c=0,1
  for i in weights:
    if t+i<11: t+=i
    else:
      t=i
      c+=1
  return c

