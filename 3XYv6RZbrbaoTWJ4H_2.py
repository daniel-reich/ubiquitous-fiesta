
def sum_cubes(n):
  arr = range(1, n+1)
  cube = map(lambda num: num**3, arr)
  return sum(list(cube))

