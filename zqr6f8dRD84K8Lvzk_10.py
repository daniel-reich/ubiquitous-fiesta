
def hex_lattice(n):
  if n==1: return " o "
  s = int(((n-1)/3)**0.5)
  if (n-1)%3 or (n-1)//3!=s*(s+1): return 'Invalid'
  a=[' '*(s+1-i)+'o '*(s+1+i)+' '*(s-i) for i in range(s+1)]
  return '\n'.join(a+a[:s][::-1])

