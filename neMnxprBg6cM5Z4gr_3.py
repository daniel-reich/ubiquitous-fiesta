
def arithmetic_progression(start, diff, n):
  res = ''
  c = start
  for i in range(n):
    res += str(c)+', '
    c+=diff
  return res[:-2]

