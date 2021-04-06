
def cap_last(txt):
  return ' '.join(i[:-1] + i[-1].upper() for i in txt.split())

