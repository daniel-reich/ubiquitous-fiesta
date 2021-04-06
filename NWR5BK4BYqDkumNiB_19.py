
def digital_division(n):
  r=""
  res=[]
  sum1=0
  prod=1
  for i in str(n):
      if not i=='0':
          r+=str(i)
  flag=True
  for i in r:
      if not int(n)%int(i)==0:
          flag=False
  if flag:
      res.append(1)
  for i in str(n):
      sum1+=int(i)
      prod*=int(i)
  if n%sum1==0:
      res.append(2)
  if not prod==0:
    if n%prod==0:
      res.append(3)
  if len(res)==3:
    return 'Perfect'
  elif len(res)==0:
    return 'Indivisible'
  else:
    return len(res)

