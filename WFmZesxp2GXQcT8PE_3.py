
def digital_cipher(message, key):
  result = []
  for i in range(len(message)):
    result.append((ord(message[i]) - 96 ) + int((str(key) * (i+1))[i]))
  return result
​
def digitalCipher(message, key):
  return digital_cipher(message, key)

