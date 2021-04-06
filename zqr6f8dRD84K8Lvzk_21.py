
def hex(x):
  return 1+3*x*(x-1)
​
def hex_lattice(n):
  c=int(((n-1)/3)**.5+1)
  if n!=hex(c): return "Invalid"
  l=r=' o'*(2*c-1) + ' '
  for i in reversed(range(c-1)):
    l=' '+l[:len(l)//2-1]+l[len(l)//2+1:]+' '
    r=l+'\n'+r+'\n'+l
  return r

