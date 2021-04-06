
def paul_cipher(s, t=None, p=None):
  if t is None: return paul_cipher(s[1:].upper(),
    s[0].upper(), [0, ord(s[0].upper()) - 64][s[0].isalpha()])
  if not len(s): return t
  c, k = s[0], ord(s[0])
  if c.isalpha():
    c = chr(((k - 64 + p) % 26) + 64)
    p = k - 64
  return paul_cipher(s[1:], t + c, p)

