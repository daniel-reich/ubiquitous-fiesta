
def digital_cipher(message, key):
  key=str(key)
  return [(ord(message[i])-96)+int(key[i%len(key)]) for i in range(len(message))]
def digitalCipher(message, key):
  key=str(key)
  return [(ord(message[i])-96)+int(key[i%len(key)]) for i in range(len(message))]

