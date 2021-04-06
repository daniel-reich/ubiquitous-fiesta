
def pile_of_cubes(m):
  c = 1
  r = m
  x = 0
  while x < m:
    x += c*c*c
    r -= c*c*c
    c += 1
  if r == 0: 
    y = c-1 
  else: 
    y = None
  return y

