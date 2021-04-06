
def domino_chain(dominos):
  a = ""
  b = dominos
  while dominos and dominos[0]=="|":
    a += "/"
    dominos = dominos[1:]
  return a + b[len(a):]

