
def make_change(c):
  res = {'q': 0, 'd': 0, 'n': 0, 'p': 0}
  while c >= 25:
    c -= 25
    res['q'] += 1
  while c >= 10:
    c -= 10
    res['d'] += 1
  while c >= 5:
    c -= 5
    res['n'] += 1
  res['p'] += c
  return res

