
def generate_rug(n):
  rug=[n//2]*n
  for i in range(len(rug)):
    rug[i]=[rug[i]]*n
  
  iterator=1
  swap=False
  for i in range(1,n):
    for x in range(i,len(rug)-i):
      rug[x]=[a for a in rug[x][:i]]+([rug[x][i]-1]*(n-(2*i)))+[a for a in rug[x][-i:]]
      
  for i in rug:
    print(i)
  return rug

