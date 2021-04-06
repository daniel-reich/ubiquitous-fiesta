
def pile_of_cubes(m):
  cur = 0
  step = 1
  while cur<m:
    cur+=step**3
    step+=1
  return step-1 if cur==m else None

