
def censor_string(txt, lst, char):
  for i in lst:
    txt = txt.replace(i, char*len(i))
  return txt

