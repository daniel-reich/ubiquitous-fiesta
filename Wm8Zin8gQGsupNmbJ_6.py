
def binary_conversion(txt):
  x = []
  for i in range(0, len(txt), 8):
    x.append(chr(int(txt[i:i +8], 2)))
  return ''.join(x)

