
def encrypt(plncode, pad):
  keyid = pad[:5]
  pad = pad[5:]
  return keyid + "".join(str((int(a)-int(b)) % 10) for a, b in zip(plncode, pad))
​
def decrypt(cypcode, pad):
  if cypcode[:5] != pad[:5]: return "Error: Key IDs don't match."
  pad = pad[5:]
  cypcode = cypcode[5:]
  return "".join(str((int(a)+int(b)) % 10) for a, b in zip(cypcode, pad))

