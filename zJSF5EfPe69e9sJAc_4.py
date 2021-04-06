
def censor_string(txt, lst, char):
  txt = txt.split(" ")
  for x, y in enumerate(txt):
    if y in lst:
      txt[x] = char*len(txt[x])
  return " ".join(txt)

