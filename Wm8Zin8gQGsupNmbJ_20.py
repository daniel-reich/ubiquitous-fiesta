
def binary_conversion(txt):
  res = ""
  for i in range(0,len(txt),8):
    res += chr( int(txt[i:i+8],2) )
  return res

