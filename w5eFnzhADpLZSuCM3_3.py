
def multiplicity(lst):
  res = [[] for i in range(0)]
  for elmt in lst:
    found = False
    for couple in res:
      if elmt == couple[0]:
        couple[1] += 1
        found = True
    if not found:
      res.append([elmt,1])
  return res

