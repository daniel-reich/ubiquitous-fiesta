
group = lambda s1, s2: zip(map(int, s1), map(int, s2))
  
def encrypt(plncode, pad):
  key, pad = pad[:5], pad[5:]
  crypt = "".join(str((txt -  p) % 10) for txt, p in group(plncode, pad))
  return key + crypt
​
def decrypt(cypcode, pad):
  key, pad = pad[:5], pad[5:]
  keyCheck, cypcode = cypcode[:5], cypcode[5:]
  if key != keyCheck:
    return "Error: Key IDs don't match."
  return "".join(str((cryp + p) % 10) for cryp, p in group(cypcode, pad))

