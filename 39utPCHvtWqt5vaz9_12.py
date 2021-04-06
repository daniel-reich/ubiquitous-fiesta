
def direction(lst):
  replacements = {'e':'w','a':'e','E':'W','A':'E'}
  out = []
  for item in lst:  
    word = "".join([replacements.get(c, c) for c in item])
    out.append(word)
  return out

