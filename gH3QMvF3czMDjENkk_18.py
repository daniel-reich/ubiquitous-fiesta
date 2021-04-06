
def remove_letters(l, word):
  for x in word: 
    if x in l: l.remove(x)
  return l

