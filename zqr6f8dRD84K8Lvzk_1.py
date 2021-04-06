
def hex_lattice(n):
  x=(1+(1-4*(1-n)/3)**0.5)/2
  if x%1:return "Invalid"
  y=2*int(x)-1
  res,c,form=[],0,'{:^'+str(y*2+1)+'}'
  while c<=y:
    res+=[form.format(' '.join(['o']*y))]
    c+=1
    y-=1
  res=res[-1:0:-1]+res
  return '\n'.join(res)

