
def modify(txt):
  return int(bin(int(''.join([str(ord(k) - 96) for k in txt[::-1]])))[2:])

