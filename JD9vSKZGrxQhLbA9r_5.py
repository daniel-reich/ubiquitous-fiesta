
def pile_of_cubes(m: int):
  cube_sum = 0; n = 0
  while cube_sum < m:
    n += 1
    cube_sum += n ** 3
  return n if cube_sum == m else None

