
def half_a_fraction(fract):
  n, d = map(int, fract.split('/'))
  return '{}/{}'.format(n if n%2 else n//2, d*2 if n%2 else d)

