
def digital_decipher(eMessage, key):
  keyPos = 0
  key = str(key)
  
  decodeMessage = ''
  for digit in eMessage:
    decodeMessage += chr(int(digit) - int(key[keyPos])+96)
    keyPos += 1
    if (keyPos >= len(key)):
      keyPos = 0
  return decodeMessage

