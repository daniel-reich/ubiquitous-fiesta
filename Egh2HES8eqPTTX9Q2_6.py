
import string
def rolling_cipher(txt, n):
  return ''.join(string.ascii_lowercase[(string.ascii_lowercase.index(t)+n)%26] for t in txt)

