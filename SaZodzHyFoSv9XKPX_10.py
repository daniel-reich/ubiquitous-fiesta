
def domino_chain(dominos):
  dominos = list(dominos)
  for i, d in enumerate(dominos):
    if d in [' ', '/']:
      break
    dominos[i] = '/'
  return ''.join(dominos)

