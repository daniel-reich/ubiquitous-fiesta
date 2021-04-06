
def censor_string(txt, lst, char):
  for i in lst:
    if i in txt:
      txt = txt.replace(i, len(i)*char)
  return txt

