
def complete_binary(s):
  m=len(s)//8+1 if len(s)%8!=0 else len(s)//8
  return s.zfill(8*m)

