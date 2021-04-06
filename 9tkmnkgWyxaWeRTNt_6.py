
def median(l):
  l.sort()
  z=len(l)
  return l[z//2]if z%2else(l[z//2-1]+l[z//2])/2

