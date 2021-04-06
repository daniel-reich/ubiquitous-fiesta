
def dif_ciph(t):
  l,c=[],0
  if type(t)==str:
    for x in t:l.append(ord(x)-c);c=ord(x)
    return l
  for x in t:l.append(chr(x+c));c+=x
  return''.join(l)

