
def flip(txt, spec):
  txt = txt.split()
  return ' '.join(x for x in reversed(txt)) if spec == "sentence" else ' '.join(x[::-1] for x in txt)

