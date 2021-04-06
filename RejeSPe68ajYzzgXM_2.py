
def combine(lst):
  states = {e[0] for e in lst}
  FSA = {s:[None,None] for s in states}
  for e in lst:
    FSA[e[0]][e[1]] = e[2]
  return FSA

