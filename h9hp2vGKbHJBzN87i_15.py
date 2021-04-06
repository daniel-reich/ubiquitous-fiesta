
def partially_hide(phrase):
  return ' '.join([x[0] + (len(x) - 2)*'-' + x[len(x)-1] if len(x) > 1 else x for x in phrase.split(' ')])

