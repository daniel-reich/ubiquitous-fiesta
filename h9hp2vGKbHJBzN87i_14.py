
def partially_hide(phrase):
  return ' '.join([w[:1] + ('-' * (len(w) - 2)) + w[-1:] for w in phrase.split()])

