
def percent_filled(x):
  y = ''.join(x)
  o = y.count('o')
  x = y.count(' ')
  w = round(o / (o + x) * 100)
  return str(w) + '%'

