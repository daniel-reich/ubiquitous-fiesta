
def multiply(l):
  bigL = []
  smL = []
  for x in range(len(l)):
    for y in range(len(l)):
      smL.append(l[x])
    bigL.append(smL)
    smL = [] # reset
  return bigL

