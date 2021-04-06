
def simplify_frac(f):
  f=[int(i) for i in f.split('/')]
  a=f[0]
  b=f[1]
  for i in range(2,f[0]+1):
    if f[0]%i==0 and f[1]%i==0: 
      a=f[0]/i
      b=f[1]/i
  return str(int(a))+'/'+str(int(b))

