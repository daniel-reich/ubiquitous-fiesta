
def moran(n):
  s = sum(int(i) for i in str(n))
  if not n%s:
    n //= s
    if not any(not n%i for i in range(2,n)):
      return 'M'
    return 'H'
  return 'Neither'

