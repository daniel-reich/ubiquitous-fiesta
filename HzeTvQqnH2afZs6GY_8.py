
def generate_rug(n, direction):
  x=n
  a=[]
  o=[]
  v=0
  y=direction
  for i in range(x):
    for i in range(x):
      o.append(abs(i-v))
    v+=1
    if y=='left':
      a.append(o)
    else:
      a.append(o[::-1])
    o=[]
  return(a)

