
def simplify(txt):
  n = int(txt[:txt.index('/')])
  m = int(txt[txt.index('/')+1:])
  if n%m == 0:
    return str(n//m)
  for i in range(min(m,n), 0, -1):
    if m%i == 0 and n%i == 0:
      return '{}/{}'.format((n//i),(m//i))

