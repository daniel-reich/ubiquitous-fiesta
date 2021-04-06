
def batting_avg(lst):
  a, b = 0, 0
  for x, y in lst:
    a += x
    b += y
  n = round(a/b * 1000)
  return '.{}'.format(n)

