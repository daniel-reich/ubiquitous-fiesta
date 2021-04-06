
def censor_string(txt, lst, char):
  words, res = txt.split(), []
  for word in words:
    if word in lst: res.append(char*len(word))
    else: res.append(word)
  return " ".join(res)

