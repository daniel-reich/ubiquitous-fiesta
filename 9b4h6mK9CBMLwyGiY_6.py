
def get_distance(a, b):
  p=list(a.values())
  q=list(b.values())
  dis=((p[0]-q[0])**2+(p[1]-q[1])**2)**.5
  return round(dis,3)

