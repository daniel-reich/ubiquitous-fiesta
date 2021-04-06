
def digital_cipher(message, key):
  key = str(key)
  return [ord(c) - 96 + int(key[i % len(key)]) for i, c in enumerate(message)]

