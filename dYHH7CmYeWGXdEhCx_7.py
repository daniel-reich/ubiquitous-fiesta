
def word_builder(letters, positions):
  newlst = [None]*len(positions)
  for l,p in zip(letters,positions):
    newlst[p] = l
  return "".join(newlst)

