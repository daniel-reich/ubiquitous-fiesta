
def safecracker(start, increments):
  combi,x = [],-1
  for i in increments:
    combi.append((start+i*x)%100)
    x*=-1
    start=combi[-1]
  return combi

