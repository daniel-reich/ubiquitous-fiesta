
def valid_division(d):
  p,q = [int(x) for x in d.split('/')]
  return not(p%q) if q else 'invalid'

