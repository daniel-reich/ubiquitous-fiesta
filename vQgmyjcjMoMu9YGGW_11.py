
def simplify(txt):
  a, b = map(int, txt.split('/'))
  if a % b == 0:
    return str(a//b)
  for i in range(min(a, b), 1, -1):
    if a % i == 0 and b % i == 0:
      return '{}/{}'.format(a//i, b//i)
  return txt

