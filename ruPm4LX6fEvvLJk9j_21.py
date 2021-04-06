
def esthetic(n):
  e = lambda x: all(x[i:i+2] in '0123456789876543210' for i in range(len(x)))
  esth = [i for i in range(2,11) if e(convert(n,i))]
  return esth if esth else 'Anti-Esthetic'
  
def convert(n, base):
  n_b = ''
  while n:
    n_b = str(n%base) + n_b
    n = n // base
  return n_b

