
def keyboard_shortcut(n):
  n=n.replace("Ctrl ","")
  n=n.replace("+","")
  n=n.split(" ")
  x=''
  on=0
  i=0
  while(i<len(n)):
    if(n[i]!='C' and n[i]!='V'):
      x+=n[i]+' '
    if(n[i]=='C'):
      on=1
    if(n[i]=='V' and on==1):
      i-=2
      x+=x
      z='' 
      on=0
      
    i+=1
  ans=''
  x=x.split(" ")
  for i in x:
    if(i!=''):
      ans+=(i.lstrip()).rstrip()+' '
  return ans[0:len(ans)-1]

