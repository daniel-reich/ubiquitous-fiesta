
def first_index(hex_txt, needle):
  return "".join(chr(int(ch,16)) for ch in hex_txt.split()).index(needle)

