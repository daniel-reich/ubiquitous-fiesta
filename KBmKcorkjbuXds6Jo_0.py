
def chocolates_parcel(s,b,o):
  d={x:y for y in range(s+1)for x in range(b+1)if 5*x+2*y==o}
  return d[max(d)]if d else-1

