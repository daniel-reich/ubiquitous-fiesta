
def plus_sign(txt):
  return txt == "".join("+{}+".format(s) if s.isalpha() else s for s in txt.replace("+","")).replace("++","+")

