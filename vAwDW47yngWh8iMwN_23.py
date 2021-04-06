
def cap_last(txt):
  return ' '.join((w[:-1]+w[-1].upper()) for w in txt.split())

