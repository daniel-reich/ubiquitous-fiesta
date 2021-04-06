
def domino_chain(dominos):
  if dominos == "":
    return ""
  def index(string, i, char):
      return string[:i] + char + string[i+1:]
  for i, domino in enumerate(dominos):
    if domino in "/ ":
      return dominos
    dominos = index(dominos, i, "/")
    if i < len(dominos)-1 and dominos[i+1] in "/ ":
      return dominos
  return dominos

