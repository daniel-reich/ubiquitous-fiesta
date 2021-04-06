
def modify(txt):
  a = txt[::-1]
  b = list(map(lambda x: str(ord(x) - 96), a))
  c = int(''.join(b))
  d = int(bin(c)[2:])
  return d

