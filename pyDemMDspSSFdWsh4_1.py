
def digital_decipher(eMessage, key):
  key = str(key) * len(eMessage)
  return ''.join(chr(a + 96 - int(b)) for a, b in zip(eMessage, key))

