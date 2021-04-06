
def flip(txt, spec):
  txt = txt.split(' ')
  if spec == 'word':
    return ' '.join(i[::-1] for i in txt)
  elif spec == 'sentence':
    return ' '.join(i for i in txt[::-1])

