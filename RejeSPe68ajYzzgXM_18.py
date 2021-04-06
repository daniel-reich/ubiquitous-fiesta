
def combine(lst):
  fsa = {}
  for inst in lst:
    if not inst[0] in fsa:
      fsa[inst[0]] = ['', '']
    fsa[inst[0]][inst[1]] = inst[2]
  return fsa

