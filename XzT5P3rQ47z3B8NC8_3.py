
def condi_cipher(message, key, shift):
  alpha='abcdefghijklmnopqrstuvwxyz'
  key2=''
  for x in key:
    if x not in key2:
      key2+=x
  for x in alpha:
    if x not in key2:
      key2+=x
  res=''
  A=[]
  k=key2.index(message[0])
  A.append(k)
  res+=key2[(k+shift)%26]
  for i in range(1, len(message)):
    if message[i].isalpha():
      p=key2.index(message[i])
      res+=key2[(p+A[-1]+1)%26]
      A.append(p)
    else:
      res+=message[i]
  return res

