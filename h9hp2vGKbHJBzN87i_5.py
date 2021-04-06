
def partially_hide(phrase):
  return ' '.join([c[0]+'-'*(len(c)-2)+c[-1] for c in phrase.split()])

