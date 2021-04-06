
def esthetic(n):
  base_esthetic = []
  for base in range(2,11):
    m = to_base(n, base)
    if all(abs(a-b) == 1 for a,b in zip(m,m[1:])):
      base_esthetic.append(base)
  return base_esthetic or 'Anti-Esthetic'
  
def to_base(n, b):
  ''' Convert n from base 10 to base b'''
  m = []
  while n:
    m.append(n%b)
    n //= b
  return m

