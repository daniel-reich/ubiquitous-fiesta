
def convert_to_hex(txt):
  return " ".join(hex(ord(c))[2:] for c in txt)

