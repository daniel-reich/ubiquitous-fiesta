
def pile_of_cubes(m):
  total = 0
  i = 0
  while total < m:
    total += i**3
    i += 1
  return i-1 if total == m else None

