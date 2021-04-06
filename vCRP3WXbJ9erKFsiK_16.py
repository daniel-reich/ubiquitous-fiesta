
def dif_ciph(inpt):
  if isinstance(inpt, list):
    last, s = inpt[0], chr(inpt[0])
    for i in inpt[1:]:
      s += chr(last + i)
      last += i
    return s
      
  else:
    last, a = 0, []
    for i in inpt:
      a += [ord(i) - last]
      last = ord(i)
    return a

