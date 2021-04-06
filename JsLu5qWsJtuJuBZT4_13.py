
def flip(txt, spec):
  if spec== "word":
    return " ".join([x[::-1] for x in txt.split()])
  return " ".join(txt.split()[::-1])

