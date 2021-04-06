
def golomb(n,g=[1,2,2]):
  i=max(g)
  while len(g)<n:
    g+=[i+1]*g[i]
    i+=1
  return g[:n]

