
def emphasise(txt):
  return ' '.join(i[0].upper() + i[1:].lower() for i in txt.split())

