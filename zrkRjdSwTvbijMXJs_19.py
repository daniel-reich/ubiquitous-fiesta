
def encrypt(plncode, pad):
  return pad[:5] + ''.join(str((int(plncode[i])-int(pad[i+5])+10) % 10) for i in range(len(plncode)))
​
def decrypt(cypcode, pad):
  if cypcode[:5] != pad[:5]:
    return "Error: Key IDs don't match."
  else:
    return ''.join( str( (int(cypcode[i])+int(pad[i]))%10) for i in range(5, len(cypcode)) )

