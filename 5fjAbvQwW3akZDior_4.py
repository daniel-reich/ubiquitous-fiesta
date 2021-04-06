
def unrepeated(txt):
  return ''.join(ch for idx, ch in enumerate(txt) if idx == txt.index(ch))

