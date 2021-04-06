
def arithmetic_progression(start, diff, n):
  x = str(start)
  for i in range(n - 1):
    x += ", " + str(start + diff*(i + 1))
  return x

