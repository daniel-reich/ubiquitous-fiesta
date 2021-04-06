
def paul_cipher(txt):
  diff, res = 0, ''
  for c in txt.upper():
    if c.isalpha():
      n = (ord(c)-64 + diff)%26
      diff = ord(c)-64
      c = 'Z' if not n else chr(n+64)
    res += c
  return res

