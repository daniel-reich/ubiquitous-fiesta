
def unmix(txt):
  x=[]
  for i in range(0,len(txt),2):
    x.append(txt[i])
  y=[]
  for i in range(1,len(txt),2):
    y.append(txt[i])
  if len(x)<len(y):
    x.append('')
  if len(x)>len(y):
    y.append('')    
  c=[]
  for i in range(len(x)):
    c.append(y[i]+x[i])
  return ''.join(c)

