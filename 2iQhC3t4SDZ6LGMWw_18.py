
def on_rectangle_bounds(points):
  x=[]
  y=[]
  d=[]
  r=[]
  if len(points)<=2:
    return True
  for p in points:
    x.append(p[0])
    y.append(p[1])
  e=max(x)
  f=max(y)
  z=min(x)
  t=min(y)
  for p in points:
    if p[0]==e or p[0]==z:
      if p[1]<=f and p[1]>=t:
        continue
      else:
        return False
    elif p[1]==f or p[1]==t:
      if p[0]<=e and p[0]>=z:
        continue
      else:
        return False
    elif p[0]<e and p[0]>z:
      if p[1]==f or p[1]==t:
        continue
      else:
        return False
    else:
      if p[0]==e or p[0]==z:
        continue
      else:
        return False
  return True

