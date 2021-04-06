
def partially_hide(phrase):
  return ' '.join(w[0] + '-'*len(w[1:-1]) + w[-1] for w in phrase.split())

