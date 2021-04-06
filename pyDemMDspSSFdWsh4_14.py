
def digital_decipher(eMessage, key):
  Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
              'g', 'h', 'i', 'j', 'k', 'l', 
              'm', 'n', 'o', 'p', 'q', 'r', 
              's', 't', 'u', 'v', 'w', 'x', 
              'y', 'z']
  a = ""
  x = int(len(eMessage)/len(str(key)))
  y = len(eMessage)%len(str(key))
  key = x * str(key) + str(key)[0:y]
  for i in range(0, len(eMessage)):
    a = a + Alphabet[eMessage[i] - 1 - int(key[i])]
    
  return a

