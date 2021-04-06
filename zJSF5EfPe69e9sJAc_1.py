
def censor_string(txt, lst, char):
  return ' '.join(char*len(word) if word in lst else word for word in txt.split())

