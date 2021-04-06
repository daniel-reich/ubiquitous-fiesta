
def first_index(hex_txt, needle): 
  for c in hex_txt.split():
    if chr(int(c, 16)) == needle[0]:
      return hex_txt.split().index(c)

