
def binary_conversion(txt):
  l=[txt[i:i+8] for i in range(0,len(txt),8)]
  return "".join(chr(int(x,2)) for x in l)

