
def mirror_cipher(message, key='abcdefghijklmnopqrstuvwxyz'):
  ciphertext = ''
  for letter in message.lower():
    if letter in key:
      ciphertext += key[len(key) - 1 - key.index(letter)]
    else:
      ciphertext += letter
  return ciphertext

