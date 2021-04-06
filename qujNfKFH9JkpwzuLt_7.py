
def first_index(hex_txt, needle):
  s=''
  for x in hex_txt.split():
    s+=chr(int('0x'+x,16))
  return s.find(needle)

