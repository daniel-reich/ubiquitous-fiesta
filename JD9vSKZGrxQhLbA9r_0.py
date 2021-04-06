
def pile_of_cubes(m):
  vol, cubes = 1, 1
  while vol < m:
    vol += cubes**3
    cubes += 1
  return [None, cubes-1][vol-1 == m]

