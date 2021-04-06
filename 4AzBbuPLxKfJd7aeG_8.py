
def encrypt(key, message):
  KD1=[x for x in zip(key[0::2], key[1::2])]
  KD2=[x for x in zip(key[1::2], key[0::2])]
  KD=[]
  for x in KD1:
    if all(y[0]!=x[0] for y in KD):
      KD.append(x)
  KD2=[x[::-1] for x in KD]
  D=dict(KD+KD2)    
  res=''
  for x in message:
    if x in D:
      res+=D[x]
    else:
      res+=x
  return res

