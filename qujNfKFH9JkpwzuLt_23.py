
def first_index(hex_txt, needle):
  return hex_txt.index(' '.join([hex(ord(c))[-2:] for c in needle])) / 3

