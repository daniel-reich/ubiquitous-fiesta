
def sentence(words):
  w = ['an ' + x if x[0] in 'aeiou' else 'a '+ x for x in words]
  return (', '.join(w[:-1]) + ' and ' + w[-1]+ '.').capitalize()

