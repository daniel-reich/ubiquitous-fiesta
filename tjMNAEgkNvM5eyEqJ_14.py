
def unique_abbrev(abbs, words):
  for i in range(len(abbs)):
    if abbs[i] != words[i][:len(abbs[i])]:
      return False
    for j in range(len(abbs)):
      if i != j and (abbs[i] in abbs[j]):
        return False
  return True

