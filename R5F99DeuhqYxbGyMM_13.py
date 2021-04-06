
def word_builder(ltr, pos):
  w =[]
  for i in range(len(pos)):
    w.append(ltr[pos[i]])
  return ''.join(w)

