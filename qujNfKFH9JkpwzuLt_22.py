
def first_index(hex_txt, needle):
  txt = ''.join(chr(int(hex,16)) for hex in str.split(hex_txt))
  return txt.find(needle)

