
def censor_string(txt, lst, char):
  return ' '.join(w if w not in lst else char * len(w) for w in txt.split())

