
def shortestDistance(txt):
  a,b,c,d = map(int,txt.split(","))
  return round(((c-a)**2+(d-b)**2)**0.5,2)

