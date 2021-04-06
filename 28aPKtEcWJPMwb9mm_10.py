
def modify(txt):
  return int(bin(int("".join(str(ord(i) - 96) for i in txt[::-1])))[2:])

