
def digital_decipher(eMessage, key):
  key = str(key)
  while len(key) < len(eMessage):
    key += key
  return ''.join(chr(96+ (ch-int(k))) for ch, k in zip(eMessage, key))

