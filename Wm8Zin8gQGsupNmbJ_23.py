
def binary_conversion(txt):
  bits = [txt[i:i + 8] for i in range(0, len(txt), 8)]
  return ''.join([chr(int(bits[b], 2)) for b in range(len(bits))])

