
def modify(t):
  t = reversed(t)
  t = map(lambda x: str(ord(x) - 96), t)
  t = int(''.join(t))
  t = bin(t)
  t = int(t[2:])
  return t

