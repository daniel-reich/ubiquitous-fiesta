
def convert_to_hex(txt):
  x = [hex(ord(x)).replace("0x","") for x in txt]
  return ' '.join(x)

