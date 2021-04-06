
def convert_to_hex(txt):
  hexa = ""
  for char in txt:
    hexa += (hex(ord(char)))[2:] + " "
  return hexa[:-1]

