
def half_a_fraction(fract):
  num, den = map(int, fract.split('/'))
  return '{}/{}'.format(*[(num//2, den), (num, den*2)][num%2])

