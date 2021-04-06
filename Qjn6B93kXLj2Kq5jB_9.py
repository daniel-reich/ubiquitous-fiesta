
def simplify_frac(f):
  a = [int(x) for x in f.split('/')]
  b,c = a[0], a[1]
  while c:
    b,c = c,b%c
  return str(a[0]//b) + '/' + str(a[1]//b)

