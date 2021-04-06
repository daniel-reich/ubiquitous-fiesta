
def censor_string(txt, lst, r):
  return " ".join(r*len(i) if i in lst else i for i in txt.split())

