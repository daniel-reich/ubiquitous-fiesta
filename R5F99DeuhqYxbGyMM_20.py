
def word_builder(ltr, pos):
  str = ''
  for i in range(len(pos)):
    str += ltr[pos[i]]
  return str

