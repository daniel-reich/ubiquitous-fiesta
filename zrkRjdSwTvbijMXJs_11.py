
def encrypt(plncode, pad):
  cypcode=''
  for i in range(len(plncode)):
    cypcode+=str((int(plncode[i])-int(pad[i+5]))%10)
  return pad[:5]+cypcode  
​
def decrypt(cypcode, pad):
  plncode=''
  if cypcode[:5]!=pad[:5]:
    return "Error: Key IDs don't match."
  for i in range(5,len(cypcode),1):
    plncode+=str((int(cypcode[i])+int(pad[i]))%10)
  return plncode

