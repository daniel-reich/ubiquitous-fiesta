
def domino_chain(dominos):
  return dominos.replace("|", "/", min(len(dominos.split(" ")[0]), len(dominos.split("/")[0])))

