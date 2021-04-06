
def unique_abbrev(abbs, words):
  for abbr in abbs:
    if sum([x.startswith(abbr) for x in words]) > 1:
      return False
  return True

