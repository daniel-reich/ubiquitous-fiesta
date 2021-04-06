
def binary_conversion(txt):
  ascii_txt = ""
  j = 0
  for i in range(8, len(txt)+8, 8):
    ascii_txt += chr(int(txt[j:i], 2))
    j = i
  return ascii_txt

