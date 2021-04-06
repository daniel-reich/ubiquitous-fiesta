
def moran(n):
  x=str(n)
  a=[]
  o=0
  y=[]
  for i in range(1,3033):
    st=True
    for j in range(2,i):
      if i%j==0:
        st=False
    if st==True:
      a.append(i)
  for i in x:
    if i.isdigit():
      y.append(int(i))
  for i in y:
    o+=i
  if int(x)/o in a:
    return('M')
  elif int(x)%o==0:
    return('H')
  else:
    return('Neither')

