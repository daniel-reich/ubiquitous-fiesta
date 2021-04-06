
def valid_division(d):
  a, b = (int(x) for x in d.split('/'))
  return a / b == a // b if b != 0 else 'invalid'

