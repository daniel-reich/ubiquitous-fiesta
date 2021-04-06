
def modify(t):
  return int(bin(int(''.join([str(ord(i)-96) for i in t[::-1]])))[2:])

