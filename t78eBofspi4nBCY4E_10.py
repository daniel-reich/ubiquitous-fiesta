
def base_conv(n,b):
  c=[]
  s=0
  if(type(n) is int):
    while(n>b):
      c.append(n%b)
      n=int(n/b)
    c.append(n)
    return "".join(chr(97+j)  for j in c[-1::-1])
  else:
    for j in range(0,len(n)):
      if(ord(n[j])-97>=b or n[j]==' '):
        return n+' is not a base '+str(b)+" number."
      s+=(ord(n[j])-97)*(b**(len(n)-1-j))
    return s

