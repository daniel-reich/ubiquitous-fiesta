
def max_product(n):
  def digprod(n):
    prod = 1
    for d in str(n):
      prod *= int(d)
    return prod
  pds = []
  for i in range(1,n+1):
    pds.append((digprod(i),i))
  pds.sort(reverse= True)
  if pds[0][0] == pds[1][0]:
    return [pds[1][1], pds[0][1]]
  else:
    return [pds[0][1]]

