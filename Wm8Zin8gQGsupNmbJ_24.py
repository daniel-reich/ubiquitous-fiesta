
def binary_conversion(txt):
  arr = [txt[ndx:ndx+8] for ndx in range(0, len(txt), 8)]
  return ''.join([chr(int(item, 2)) for item in arr])

