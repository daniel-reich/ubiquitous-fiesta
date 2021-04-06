
def flip(txt, spec):
  if spec == 'word':
    return ' '.join([i[::-1] for i in txt.split()])
  return ' '.join(reversed(txt.split(' ')))

