
def first_index(hex_txt, needle):
  return ''.join(chr(int(i, 16)) for i in hex_txt.split()).index(needle)

