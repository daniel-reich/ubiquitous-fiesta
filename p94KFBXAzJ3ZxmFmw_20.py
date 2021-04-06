
def ascii_capitalize(txt):
  l = list(txt)
  for i in range(len(l)): l[i] = l[i].upper() if(ord(l[i])%2==0) else l[i].lower()
  return ''.join(map(str, l))

