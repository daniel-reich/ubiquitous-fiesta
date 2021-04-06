
def first_index(hex_txt, needle):
  h=hex_txt.split()
  lst=[]
  for n in h:
    lst.append(chr(int(n,16)))
  return lst.index(needle[0])

