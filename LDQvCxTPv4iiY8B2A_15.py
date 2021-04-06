
def same_upsidedown(ntxt):
  n=str(ntxt)
  k=n[-1::-1]
  l=''
  for i in k:
    if(i=='9'): 
      l+='6'
    elif(i=='6'):
      l+='9'
    else:
      l+=i
  return l==n

