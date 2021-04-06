
def encrypt(plncode, pad):
  kID,pad = pad[:5],pad[5:]
  ret = ""
  for i in range(len(plncode)):
    a = int(plncode[i])
    b = int(pad[i])
    if a<b:
      a+=10
    ret+=str((a-b)%10)
  return kID+ret
  
def decrypt(cypcode, pad):
  kID,pad = pad[:5],pad[5:]
  if not cypcode.startswith(kID):
    return "Error: Key IDs don't match."
  cypcode = cypcode[5:]
  ret = ""
  for i in range(len(cypcode)):
    a = int(cypcode[i])
    b = int(pad[i])
    ret+=str((a+b)%10)
  return ret

