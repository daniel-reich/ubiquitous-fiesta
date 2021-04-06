
def half_a_fraction(fract):
  fract = fract.split('/')
  c = [int(i) for i in fract]
  return '{}/{}'.format(round(c[0] /2 if c[0]%2 == 0 else c[0]) , round(c[1]* 2 if c[0] % 2 ==1 else c[1]))

