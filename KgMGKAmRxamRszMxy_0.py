
def spartans_cipher(m,n):
  if not m:return''
  l=-(-len(m)//n)
  m=m.ljust(l*n,' ')
  p=[m[i:i+l]for i in range(0,len(m),l)]
  return''.join([p[i][j]for j in range(l)for i in range(n)]).strip()

