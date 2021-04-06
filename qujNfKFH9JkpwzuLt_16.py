
def first_index(hex_txt, needle):
  word = ''.join( [ chr(int(x,16)) for x in hex_txt.split() ] )
  return word.index(needle)

