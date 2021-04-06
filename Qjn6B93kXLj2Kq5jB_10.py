
def simplify_frac(f):
  a,b=f.split('/')
  r=[i for i in range(1,int(a)+1) if int(a)%i==0]
  g=[j for j in range(1,int(b)+1) if int(b)%j==0]
  v=max(list(set(r).intersection(set(g))))
  x=int(a)//v
  y=int(b)//v
  return str(x)+'/'+str(y)

