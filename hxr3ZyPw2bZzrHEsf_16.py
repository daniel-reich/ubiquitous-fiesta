
def make_title(txt):
  new=""
  for t in txt.split(" "):
    new += t[0].upper() + t[1:] + " "
  return new.strip()

