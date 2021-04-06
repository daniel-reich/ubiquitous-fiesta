
def binary_conversion(txt):
  return "".join(chr(int(txt[i:i + 8], 2)) for i in range(0, len(txt), 8))

