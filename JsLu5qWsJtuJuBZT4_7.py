
def flip(txt, spec):
  if spec == 'word':
    return " ".join(i[::-1] for i in txt.split(" "))
  else:
    return " ".join(i for i in txt.split(" ")[::-1])

