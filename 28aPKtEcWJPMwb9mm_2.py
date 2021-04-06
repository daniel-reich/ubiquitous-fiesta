
def modify(txt):
  res = ''.join([str(ord(i) - 96) for i in txt[::-1]])
  return int(bin(int(res))[2:])

