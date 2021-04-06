
def censor_string(txt, lst, char):
  for x in lst:
    txt=txt.replace(x,char*len(x))
  return txt

