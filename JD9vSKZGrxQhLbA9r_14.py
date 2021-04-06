
def pile_of_cubes(m):
  n, i = 0, 0
  while n < m:
    i += 1
    n += i ** 3
  if n == m:
    return i

