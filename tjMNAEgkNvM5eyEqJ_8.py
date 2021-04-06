
def unique_abbrev(abbs, words):
  for ab in abbs:
    matches = 0
    for w in words:
      if ab == w[:len(ab)]: matches += 1
    if matches > 1: return False
  return True

