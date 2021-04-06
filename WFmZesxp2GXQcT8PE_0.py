
def digital_cipher(message, key):
  k=list(map(int,str(key)))
  l=len(k)
  return [ord(x)-96+k[i%l] for i,x in enumerate(message)]

