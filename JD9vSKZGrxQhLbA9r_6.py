
def pile_of_cubes(m):
  count = 0
  volume = 0
  while (volume < m):
    count += 1
    volume += count ** 3
  return [None, count][volume == m]

