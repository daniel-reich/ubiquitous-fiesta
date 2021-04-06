
def remove_letters(l, w):
  w = list(w)
  return [k for k in [i if i not in w else w.remove(i) for i in l] if k != None]

