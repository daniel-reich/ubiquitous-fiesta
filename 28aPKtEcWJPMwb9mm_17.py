
def modify(txt):
  a = int(''.join(str(ord(x) - 96) for x in txt[::-1]))
  return int(str(bin(a))[2:])

