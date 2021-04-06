
def flip(txt, spec):
  if spec == "word":
    txt = txt.split()
    return " ".join(t[::-1] for t in txt)
  else: 
    txt = txt.split()
    txt.reverse()
    return " ".join(txt)

