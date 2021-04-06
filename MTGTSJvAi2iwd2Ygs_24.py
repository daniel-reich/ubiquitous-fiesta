
def valid_division(d):
  num, den = map(int, d.split('/'))
  return 'invalid' if den == 0 else num%den == 0

