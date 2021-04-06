
def maya_number(n):
  p, i = [], 0
  while n:
    v = n%(20**(i+1))
    p.insert(0,build_string(v//(20**i)))
    n, i = n-v, i+1
  return p if p else ['@']
  
def build_string(n):
  if n == 0:
    return '@'
  else:
    return 'o'*(n%5) + '-'*(n//5)

