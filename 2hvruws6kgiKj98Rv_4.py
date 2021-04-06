
def to_scottish_screaming(txt):
  caps = txt.upper()
  caps = caps.replace("A","E")
  caps = caps.replace("I","E")
  caps = caps.replace("O","E")
  caps = caps.replace("U","E")
  return caps

