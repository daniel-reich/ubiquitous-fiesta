
def encrypt(plncode, pad):
  return pad[:5] + ''.join(str((int('1'+plncode[i])-int(pad[i+5]))%10) for i in range(len(plncode)))
  
def decrypt(cypcode, pad):
  return "Error: Key IDs don't match." if cypcode[:5]!=pad[:5] else ''.join(str((int(cypcode[i])+int(pad[i]))%10) for i in range(len(cypcode)))[5:]

