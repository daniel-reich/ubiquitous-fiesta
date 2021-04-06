
def binary_conversion(s):
  res = ''
  for i in range(len(s)//8):
    res += chr(int(s[8*i:8*i+8], 2))
  return res

