
def camelCasing(txt):
  txt = txt.replace("_", " ").split()
  return txt[0].lower() + "".join(x.title() for x in txt[1:])

