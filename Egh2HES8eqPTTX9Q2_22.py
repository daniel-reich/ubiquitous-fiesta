
import string as s
def rolling_cipher(txt, n):
  return ''.join([s.ascii_lowercase[(s.ascii_lowercase.index(i) + n)%26] for i in txt])

