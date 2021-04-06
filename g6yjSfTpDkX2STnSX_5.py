
def convert_to_hex(txt):
  ascii_list = [ord(x) for x in txt]
  hex_list = [hex(y)[2:] for y in ascii_list]
  return ' '.join(hex_list)

