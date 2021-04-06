
def absolute(txt):
  return " ".join(w + "n absolute" if w.lower() == "a" else w for w in txt.split())

