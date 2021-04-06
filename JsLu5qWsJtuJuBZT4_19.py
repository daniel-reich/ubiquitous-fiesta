
def flip(txt, spec):
  if spec == "word":
    return " ".join(w[::-1] for w in txt.split())
  else:
    return " ".join(txt.split()[::-1])

