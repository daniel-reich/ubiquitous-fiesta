
def digital_decipher(eMessage, key):
  key = [int(i) for i in str(key)]
  eMessage = [chr((eMessage[i]-key[i%len(key)])+ord("a")-1) for i in range(len(eMessage))]
  
  return "".join(eMessage)

