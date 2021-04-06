
def binary_conversion(txt):
  chars = [txt[0+i:8+i] for i in range(0, len(txt), 8)]
  return ''.join(chr(int(char, 2)) for char in chars)

