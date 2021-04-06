
def high_low(txt):
  n = list(map(int,txt.split()))
  return '{} {}'.format(max(n), min(n))

