
def digital_decipher(eMessage, key):
  return "".join((chr(96 + n - int(str(key)[i % len(str(key))])) for i,n in enumerate(eMessage)))

