
def emphasise(txt):
  sep = txt.split()
  sep = [sep.capitalize() for sep in sep]
  return " ".join(sep)

