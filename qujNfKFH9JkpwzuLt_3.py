
def first_index(hex_txt, needle):
  ch1=format(ord(needle[0]),"x")
  l=hex_txt.split(" ")
  return(l.index(ch1))

