
def map_letters(word):
  w=list(str(word))
  return {l:[i for i,v in enumerate(w) if v==l] for l in w}

