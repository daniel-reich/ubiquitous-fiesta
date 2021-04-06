
def absolute(txt):
  return " ".join(x+"n absolute" if x.lower()=="a" else x for x in txt.split())

