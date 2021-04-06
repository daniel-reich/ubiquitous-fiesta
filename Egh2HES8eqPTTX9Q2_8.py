
def rolling_cipher(txt, n):
  return ''.join([chr((ord(i) - 97 + n) % 26 + 97) for i in txt])

