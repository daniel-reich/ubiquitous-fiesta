
def pile_of_cubes(m):
  c = 0
  v = 0
  count = 0
  while v < m:
    c += 1
    v += c**3
    count += 1
  if v == m:
    return count
  return None

