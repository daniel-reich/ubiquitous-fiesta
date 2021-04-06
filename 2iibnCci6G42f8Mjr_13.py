
def guess_score(code, guess):
  b,w = 0,0
  c,g = [char for char in code],[char for char in guess]
  r,l = [],len(c)
  i=0
  while i<l:
    if c[i]==g[i]:
      del c[i];del g[i]
      i,l,b=i-1,l-1,b+1
    i+=1
  for i in range(len(c)):
    for j in range(len(g)):
      if c[i]==g[j]:
        del g[j]
        i,w=i-1,w+1
        break
  return {"black":b,"white":w}

