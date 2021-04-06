
def rolling_cipher(txt, n):
  enc=""
  for t in txt:
    enc+=chr((ord(t)+n-97)%26+97)
  return enc

