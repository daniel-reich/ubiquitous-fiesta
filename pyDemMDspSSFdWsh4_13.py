
def digital_decipher(eMessage, key):
  k=list(map(int,str(key)))
  l=len(k)
  return "".join(chr(x+96-k[i%l]) for i,x in enumerate(eMessage))

