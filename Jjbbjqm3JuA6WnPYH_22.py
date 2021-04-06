
def bit_rotate(n, m, d):
  x=str(bin(n))[2:]
  m=m%len(x)
  if(d):
    z=int(x[len(x)-m:]+x[0:len(x)-m],2)
    
  else:
    z=int(x[m:]+x[0:m],2)
  return z

