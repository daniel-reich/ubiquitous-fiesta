
def unique_abbrev(abbs, words):
  for ab in abbs:
    counter = 0
    for word in words:
      if word.startswith(ab):
        counter += 1
    if counter > 1:
      return False
  return True

