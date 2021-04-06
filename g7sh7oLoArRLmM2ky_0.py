
chars = [chr(i) for i in range (97,123)]+[None for i in range (4)]+["."," "]
​
def baconify(msg,mask=None):
  if mask==None:
    msg = [c for c in msg if c.isalpha()]
    output = ""
    for i in range (0,len(msg)-4,5):
      n = 0
      for j in range (5):
        if msg[i+j].islower():
          n += 2**(4-j)
      output += chars[n]
    return output
  msg = [c.lower() for c in msg if c.lower() in chars]
  mask = [c.lower() for c in mask]
  i = 0
  for c in msg:
    n = chars.index(c.lower())
    for j in range (4,-1,-1):
      while not mask[i].isalpha():
        i += 1
      if not n >> j & 1:
        mask[i] = mask[i].upper()
      i += 1
  return "".join([c for c in mask])

