
def unique_abbrev(abbs, words):
  for abb in abbs:
    for word in words:
      if len([word for word in words if word.startswith(abb) == True]) > 1:
        return False
  return True

