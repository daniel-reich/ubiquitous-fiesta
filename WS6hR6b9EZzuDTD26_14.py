
def no_duplicate_letters(phrase):
  wds = phrase.split()
  for w in wds:
    for l in w:
      if w.count(l) > 1:
        return False
  return True

