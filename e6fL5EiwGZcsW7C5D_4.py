
def alph_num(txt):
  st=""
  for i in range(len(txt)):
    if i!=0:
      st+=' '
    st+=str(ord(txt[i].upper())-65)
  return st

