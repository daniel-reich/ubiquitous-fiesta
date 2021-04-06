
def digital_decipher(eMessage, key):
  key=str(key)*(len(eMessage)//len(str(key))+1)
  return "".join(chr(96+x-int(y)) for x,y in zip(eMessage, key))

