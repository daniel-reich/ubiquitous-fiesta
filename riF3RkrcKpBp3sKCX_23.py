
def cap_space(txt):
  return "".join([" " + i.lower() if i.isupper() else i for i in txt])

