
def sum_cubes(n):
  result = 0
  while n > 0:
    result = result + n ** 3
    n = n - 1
  return result

