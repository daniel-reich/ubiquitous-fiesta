
def make_title(txt):
  x = txt.split(" ")
  return " ".join(i[0].upper() + i[1:] for i in x )

