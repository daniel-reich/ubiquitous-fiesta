
def mixed_number(frac):
  if frac.split('/')[0] == '0':
    return '0'
  num, den = [int(i) for i in frac.split('/')]
  string = ''
  if abs(num) > den:
    string += str(abs(num) // den)
  num = abs(num) % den
  num, den = num // (gcd(num,den)), den // (gcd(num,den))
  if abs(num) > 0:
    if len(string) > 0:
      string += ' '
    string += str(num) + '/' + str(den)
  if '-' in frac:
    string = '-' + string
  return string
    
def gcd(x,y):
  while(y):
    x,y = y, x%y
  return x

