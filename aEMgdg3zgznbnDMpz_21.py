
def rotated_words(txt):
  sym = "HIMNOSWXZ"
  ret = []
  for w in txt.split():
    if all(c in sym for c in w):
      if w not in ret:
        ret.append(w)
  return len(ret)

