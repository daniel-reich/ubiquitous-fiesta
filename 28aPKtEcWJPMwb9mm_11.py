
def modify(txt):
  nu=''.join([str(ord(x)-96) for x in txt[::-1]])
  return int(bin(int(nu))[2:])

