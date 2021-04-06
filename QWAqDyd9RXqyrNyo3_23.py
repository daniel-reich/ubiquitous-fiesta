
def abbreviate(sentence, n=4):
  return "".join(w[0] for w in sentence.upper().split() if len(w)>=n)

