
def half_a_fraction(fract):
  a, b = fract.split('/')
  a, b = int(a), int(b)
  b = b*2 if a%2 else b
  a = a//2 if not a%2 else a
  return '{}/{}'.format(a, b)

