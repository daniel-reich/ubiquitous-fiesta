
def encrypt(plncode, pad):
  res = pad[:5]
  for i in range(len(plncode)):
    res += str((int(plncode[i]) - int(pad[i+5]))%10)
  return res
  
def decrypt(cypcode, pad):
  if pad[:5] != cypcode[:5]:
    return "Error: Key IDs don't match."
  res = ""
  for i in range(5,len(cypcode)):
    res += str((int(cypcode[i]) + int(pad[i]))%10)
  return res

