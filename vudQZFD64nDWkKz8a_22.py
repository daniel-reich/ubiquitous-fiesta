
def grant_the_hint(txt):
  res = []  
  for x in range(len(max(txt.split(),key=len))+1):
    res.append([i[:x] + '_'*(len(i)-x) for i in txt.split()])
  return [' '.join(x) for x in res]

