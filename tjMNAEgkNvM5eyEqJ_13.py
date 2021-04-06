
def unique_abbrev(abbs, words):
  return all(
    sum(w.startswith(a) for w in words) == 1 
    for a in abbs
  )

