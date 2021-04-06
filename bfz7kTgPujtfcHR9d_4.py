
def x_pronounce(sentence):
  lst = ['ecks' if w == 'x' else w for w in sentence.split()]
  lst = ['z'+w[1:] if w.startswith('x') else w for w in lst]
  return ' '.join([w.replace('x', 'cks') for w in lst])

