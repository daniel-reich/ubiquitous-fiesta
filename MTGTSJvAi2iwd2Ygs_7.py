
def valid_division(d):
  D, d = (int(i) for i in d.split('/'))
  return not D%d if d else 'invalid'

