
def cap_last(txt):
  return ' '.join(i[:-1]+i.upper()[-1] for i in txt.split())

