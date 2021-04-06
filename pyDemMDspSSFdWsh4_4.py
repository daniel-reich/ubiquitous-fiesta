
def digital_decipher(eMessage, key):
  a = ' abcdefghijklmnopqrstuvwxyz'
  return ''.join(a[m-int(k)] for m, k in zip(eMessage, str(key)*100))

