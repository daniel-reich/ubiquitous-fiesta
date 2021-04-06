
def caesar_cipher(txt, key):
  return ''.join(chr(65+(ord(c)-65+key)%26) if c.isupper() else\
  chr(97+(ord(c)-97+key)%26) if c.islower() else c for c in txt)

