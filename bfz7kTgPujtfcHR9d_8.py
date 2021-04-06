
def x_pronounce(txt):
​
  txt = [ w.replace('x','ecks') if not len(w)-1 else w for w in txt.split() ]
  txt = [ w[0].replace('x','z') + w[1:] if w[0] == 'x' else w for w in txt ]
  return ' '.join(txt).replace('x','cks')

