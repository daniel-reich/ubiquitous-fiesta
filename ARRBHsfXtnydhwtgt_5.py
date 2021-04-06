
def compress(c):
​
  return compress_old(c)
  
  
def compress_old(chars):
  ct,last=0,''
  out=''
  for c in chars:
    if last==c:
      ct+=1
    else:
      out+=last+ (str(ct) if ct>1 else '' )
      ct,last=1,c
  return out+last+(str(ct) if ct>1 else '' )

