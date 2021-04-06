
def combine(lst):
  maxnum = max([inst[1] for inst in lst])
  res = {}
  for inst in lst:
    A, B, C = inst[0], inst[1], inst[2]
    if A not in res:
      res[A] = [None]*(maxnum+1)
    res[A][B] = C
  return res

