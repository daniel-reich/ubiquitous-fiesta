
def digital_cipher(message, key):
  keys = str(key)
  while len(keys) < len(message):
    keys *= 2
  return [(ord(ch)-96) + int(k) for ch, k in zip(message, keys)]

