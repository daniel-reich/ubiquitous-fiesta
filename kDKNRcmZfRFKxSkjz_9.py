
def unmix(txt):
  a = list(txt)
  b = len(a) if len(a)%2==0 else len(a)-1
  
  for i in range(0, b, 2):
    a[i], a[i+1] = a[i+1], a[i]
  
  return ''.join(a)

