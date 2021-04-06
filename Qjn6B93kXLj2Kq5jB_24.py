
def simplify_frac(f):
  fs = f.split('/')
  num = int(fs[0])
  den = int(fs[1])
  for i in reversed(range(num+1)):
    if num%i==0 and den%i==0:
      return str(num//i)+'/'+str(den//i)

