
def first_index(hex_txt,needle):
  n = hex(ord(needle[0]))[2:]
  return hex_txt.split().index(n)

