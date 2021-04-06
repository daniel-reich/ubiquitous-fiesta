
def cap_last(txt):
  return " ".join(t[:-1]+t[-1].capitalize() for t in txt.split())

