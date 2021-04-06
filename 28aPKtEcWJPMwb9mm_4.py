
def modify(txt):
  return int(bin(int(''.join([str(ord(x)-ord('a')+1) for x in txt[::-1]])))[2:])

