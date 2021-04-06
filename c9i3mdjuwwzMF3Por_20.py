
def bemirp(n):
  def is_prime(n):
    for i in range(2,n):
      if n%i == 0:
        return False
    return True
  if not is_prime(n):
    return 'C'
  l = list(str(n))
  l.reverse()
  i = ''
  for j in l:
    i += j
  if not is_prime(int(i)) or int(i) == n:
    return 'P'
  upside = ''
  for ch in str(n):
    if ch not in '10968':
      return 'E'
    if ch == '9':
      ch = '6'
    elif ch == '6':
      ch = '9'
    upside += ch
  if is_prime(int(upside)):
    return 'B'
  else:
    return 'E'

