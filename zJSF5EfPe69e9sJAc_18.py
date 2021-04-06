
def censor_string(txt, lst, char):
  for i in range(len(lst)):
    txt=txt.replace(lst[i],char*len(lst[i]))
  return txt

