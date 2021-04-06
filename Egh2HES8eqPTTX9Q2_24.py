
def rolling_cipher(txt, n):
  m=''.join(chr(i) for i in range(97,123))
  return ''.join(m[(m.index(c)+n)%26] for c in txt)

