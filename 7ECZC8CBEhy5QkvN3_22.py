
def how_many_walls(n, w, h):
  area=w*h
  if area<n:
    walls=n/area
    return int(walls)
  elif area==n:
    return 1 
  else:
    return 0

