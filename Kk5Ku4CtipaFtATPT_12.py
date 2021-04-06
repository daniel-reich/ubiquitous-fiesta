
def coconut_translator(txt):
  x=''
  for i in txt:
    print(ord(i))
    z=str(bin(ord(i)))[2:]
    while(len(z)!=8):
      z='0'+z
    x=x+z+' '
  x=x[:len(x)-1]
  z='coconuts'
  t=''
  j=0
  print(x)
  for i in x:
    if(i==' '):
      t+=' '
    elif(i=='0'):
      t+=z[j]
      j+=1
    else:
      t+=z[j].upper()
      j+=1
    if(j==len(z)):
      j=0
  return t

