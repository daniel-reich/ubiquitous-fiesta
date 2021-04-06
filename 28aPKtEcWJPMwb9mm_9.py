
def modify(txt):
  return int(bin(int(''.join(str(ord(char)-96) for char in txt[::-1])))[2:])

