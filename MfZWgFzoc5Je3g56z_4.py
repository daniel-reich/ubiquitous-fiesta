
def translate(r, n):
  r = r**2
  if n>r: return '{} is not in the range [0:{}]'.format(n,r)
  m = (r-n)%(r+1)
  if (m-n)%(r+1)<(n-m)%(r+1) or (m-n)%(r+1)==0:
    return '+{} ---> {}'.format((m-n)%(r+1),m)
  elif (m-n)%(r+1)>(n-m)%(r+1):
    return '-{} ---> {}'.format((n-m)%(r+1),m)
  else:
    return '+{} or -{} ---> {}'.format((m-n)%(r+1),(m-n)%(r+1),m)

