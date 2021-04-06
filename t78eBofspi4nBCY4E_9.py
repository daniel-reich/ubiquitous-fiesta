
def base_conv(n,b):
  if isinstance(n,int):
    return base(n,b)
  else:
    return dig(n,b)
  
def base(n,b):
  blst = 'abcdefghijklmnopqrstuvwxyz'
  ret = ''
  while n>0:
    ret+=blst[n%b]
    n=n//b
  return ret[::-1]
  
def dig(s,b):
  blst = 'abcdefghijklmnopqrstuvwxyz'
  ret = 0
  s=s[::-1]
  for i in range(len(s)):
    if s[i] not in blst[:b]:
      return s[::-1]+' is not a base '+str(b)+' number.'
    ret+=blst.index(s[i])*(b**i)
  return ret

