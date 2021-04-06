
def unique_abbrev(abbs, words):
  return all(sum(w.startswith(a) for a in abbs) == 1 for w in words)

