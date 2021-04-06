
def convert_to_hex(txt):
  return " ".join([ hex(ord(x))[2:] for x in txt ])

