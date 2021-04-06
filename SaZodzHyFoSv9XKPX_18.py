
def domino_chain(dominos):
  emptystring = ''
  for i in range(len(dominos)):
    if dominos[i] == ' ' or dominos[i] == '/':
      emptystring += dominos[i:]
      break
    else:
      emptystring += '/';
  return emptystring

