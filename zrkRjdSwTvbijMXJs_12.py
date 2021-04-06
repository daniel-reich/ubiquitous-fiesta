
def encrypt(plncode, pad):
  return pad[:5]+''.join(str((int(plncode[i])-int(pad[i+5]))%10) for i in range(0,len(plncode)))
​
def decrypt(cypcode, pad):
  return "Error: Key IDs don't match." if not cypcode[:5]==pad[:5] else ''.join(str((int(cypcode[i])+int(pad[i]))%10) for i in range(5,len(cypcode)))

