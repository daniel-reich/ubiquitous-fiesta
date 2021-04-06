
def flip(txt, spec):
  if spec == "word":
    return ' '.join([x[::-1] for x in txt.split()])
  return ' '.join([x for x in txt.split()][::-1])

