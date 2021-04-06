
def first_index(hex_txt, needle):
  return [chr(int("0x" + x,16)) for x in hex_txt.split()].index(needle[0])

