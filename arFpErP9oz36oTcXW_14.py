
def secret(txt):
  txt = txt.split(".")
  return "<{} class='{}'></{}>".format(txt[0], " ".join(txt[1:]), txt[0])

