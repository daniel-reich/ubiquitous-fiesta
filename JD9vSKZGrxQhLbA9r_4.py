
def pile_of_cubes(m):
  n = 0
  total = 0
  
  while (total <= m):
    if total == m:
      return n
    n += 1
    total += n**3

