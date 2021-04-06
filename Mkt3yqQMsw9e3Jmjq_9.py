
def disjoint_cycle_form(perm):
  visited = [False] * len(perm)
  res = set()
  for bIdx in range(len(perm)):
    if not visited[bIdx]:
      curLoop = [bIdx]
      visited[bIdx] = True
      cIdx = perm[bIdx]
      while cIdx != bIdx:
        curLoop.append(cIdx)
        visited[cIdx] = True
        cIdx = perm[cIdx]
      if len(curLoop) > 1:
        res.add(tuple(curLoop))
  return res

