
def valid_division(d):
  numerator, denominator = d.split('/')
  if int(denominator) == 0:
    return 'invalid' 
  return True if int(numerator) % int(denominator) == 0 else False

