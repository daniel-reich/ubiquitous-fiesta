
def simplify_frac(f):
  [a,b] = [int(i) for i in f.split('/')]
  return '{}/{}'.format(a//gcf(a,b), b//gcf(a,b))
​
def gcf(a,b):
  return a if not b else gcf(b,a%b)

