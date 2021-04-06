
def vigenere(n, key):
  code=1
  if(' ' in n):
    code=0
  
  key=key.upper() 
  n=n.replace(" ","")
  n=n.upper()
  nn=''
  for i in n:
    if(i>='A' and i<='Z'):
      nn+=i
  x=''
  x+=key
  i=0
  while(len(x)<len(nn)):
    if(i>=len(key)):
      i=0
    x+=key[i]
    i+=1
  a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  z=list()
  for i in range(0,len(a)):
    xx=a[i:len(a)]
    if(i!=0):
      xx.extend(a[0:i])
    z.append(xx)
  ans=''  
  print(nn,x)
  if(code==0):
    for i in range(0,len(nn)):
      ans+=z[z[0].index(nn[i])][z[0].index(x[i])]
  else:
    for i in range(0,len(x)): 
      ans+=z[0][z[z[0].index(x[i])].index(nn[i])] 
  return ans

