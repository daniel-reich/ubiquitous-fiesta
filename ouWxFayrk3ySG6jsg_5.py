
def who_won(b):
  a=list(zip(b[0],b[1],b[2]))
  c=[b[i][j] for i in range(len(a)) for j in range(len(a)) if i==j] 
  d=[b[i][j] for i in range(len(a)) for j in range(len(a)) if i+j==2]
  
  if len(set(c))==1:
    return c[0]
  if len(set(d))==1:
    return d[0]
  
  for i in range(len(b)):
    if len(set(a[i]))==1:
      return a[i][0]
    if len(set(b[i]))==1:
      return b[i][0]

