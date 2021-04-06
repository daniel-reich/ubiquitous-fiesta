
def first_index(hex_txt, needle):
  txt = ''.join([chr(int(i,16)) for i in hex_txt.split()])
  for i in range(len(txt)):
    if txt[i:i+len(needle)] == needle:
      return i

