
def x_pronounce(sentence):
  r = []
  for w in sentence.split():
    if len(w) > 1 and w[0] is 'x':
      r.append('z' + w[1:])
    elif w is 'x':
      r.append('ecks')
    else:
      r.append(w.replace('x', 'cks'))
  return ' '.join(r)

