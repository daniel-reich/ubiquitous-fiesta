
import string
def digital_decipher(eMessage, key):
  dicty=" "+string.ascii_lowercase
  keylst = list(str(key))
  num=len(eMessage)-len(keylst)
  i=0
  while i<=num-1:
    keylst.append(keylst[i%len(keylst)])
    i+=1
  keyint = list(int(x) for x in keylst)
  return "".join(dicty[x-y] for x,y in zip(eMessage,keyint))

