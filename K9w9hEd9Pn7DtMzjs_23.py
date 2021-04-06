
def high_low(txt):
  x = [int(i) for i in txt.split()]
  return '{} {}'.format(max(x), min(x))

