
def modify(txt):
  a = "".join(str(ord(i)-96) for i in txt[::-1])
  return int(str(bin(int(a)))[2:])

