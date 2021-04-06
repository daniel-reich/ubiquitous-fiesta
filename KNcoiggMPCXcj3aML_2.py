
def number_of_days(c):
  n = abs(c[0]) + abs(c[1])
  if n == 0: return 0
  if n%5 == 0:
    return n + n//5 - 1
  return n + n//5

