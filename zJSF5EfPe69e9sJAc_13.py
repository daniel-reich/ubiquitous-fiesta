
def censor_string(txt, lst, char):
  text = list()
  text = txt.split()
  index = 0
  for x in text:
    if x in lst:
      text[index] = char * len(x)
    index += 1
  return " ".join(text)

