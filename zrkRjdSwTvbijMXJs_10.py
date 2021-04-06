
def encrypt(plncode, pad):
  ans = pad[:5]
  pad = pad[5:]
  for i in range(len(plncode)):
    ans += str((int(plncode[i]) - int(pad[i])) % 10)
  return ans
  
def decrypt(cypcode, pad):
  check = pad[:5]
  if cypcode[:5] != check:
    return "Error: Key IDs don't match."
  ans = ''
  cypcode = cypcode[5:]
  pad = pad[5:]
  for i in range(len(cypcode)):
    ans += str((int(cypcode[i]) + int(pad[i])) % 10)
  return ans

