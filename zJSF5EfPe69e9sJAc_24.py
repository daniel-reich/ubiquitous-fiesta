
def censor_string(txt, lst, char):
  for word in lst :
    txt=txt.replace(word,char*len(word))
  return txt

