
def sexy_primes(n, limit):
  x=limit
  y=n
  a=[]
  k=[]
  final=[]
  for i in range(2,x):
    st=True
    for j in range(2,i):
      if i%j==0:
        st=False
    if st==True:
      a.append(i)
  for i in range(len(a)):
    if y==2:
      if a[i]+6 in a:
        k.append(a[i])
        k.append(a[i]+6)
        final.append(tuple(k))
        k=[]
    else:
      if a[i]+6 in a and a[i]+12 in a:
        k.append(a[i])
        k.append(a[i]+6)
        k.append(a[i]+12)
        final.append(tuple(k))
        k=[]
  return(final)

