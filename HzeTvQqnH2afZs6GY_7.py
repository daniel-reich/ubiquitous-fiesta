
def generate_rug(a,d):
  lis=[]
  for i in range(a):
    lisa=[]
    while len(lisa)<a:
      lisa.append(0)
    lis.append(lisa)
  i=0
  while i<a:
    lisa=[i for i in range(a-i)]
    lisum=[i for i in range(i,len(lis))]
    for j,k in zip(lisum,lisa):
      lis[i][j]=k
      lis[j][i]=k
    i+=1
  if d=="left":
    return lis
  elif d=="right":
    return lis[::-1]

