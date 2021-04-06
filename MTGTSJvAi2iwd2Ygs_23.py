
def valid_division(d):
  t,b = d.split('/')
  return int(t)%int(b) == 0 if b!= '0' else 'invalid'

