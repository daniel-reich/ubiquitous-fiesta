
def abbreviate(sentence, n = 4):
  return "".join(x[0].upper() for x in sentence.split() if len(x) >= n)

