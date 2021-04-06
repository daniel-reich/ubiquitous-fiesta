
def unique_abbrev(abbs, words):
  return all( not w.startswith(a) if i2 != i1 else w.startswith(a) for i1, w in enumerate(words) for i2, a in enumerate(abbs) )

