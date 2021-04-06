
def clockwise_cipher(message):
  k=1
  while k**2<len(message):
    k+=1
  message=message+' '*(k**2-len(message))
  res=[[0 for _ in range(k)] for _ in range(k)]
  A=[]
  for i in range(k-1):
    for j in range(k-1):
      if all(x not in A for x in [(i,j), (j,k-i-1), (k-i-1,k-j-1), (k-j-1,i)]):
        A+=[(i,j), (j,k-i-1), (k-i-1,k-j-1), (k-j-1,i)]
  D=[]
  for x in A:
    if x not in D:
      D.append(x)
  c=0
  for x in D:
    res[x[0]][x[1]]=message[c]
    c+=1
  res2=[''.join(x) for x in res]
  return ''.join(res2)

