
def flip(txt, spec):
  if spec == 'sentence':
    return ' '.join([x for x in txt.split()][::-1])
  else:
    return ' '.join([x[::-1] for x in txt.split()])

