
def unmix(txt):
  st1=""
  while (len(txt)>2):
      st1+=txt[0:2][::-1]
      txt=txt[2:]
  st1+=txt[0:2][::-1]
  return st1

