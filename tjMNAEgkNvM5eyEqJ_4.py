
def unique_abbrev(abbs, words):
  for i in range(len(abbs)):
    for j in range(len(words)):
      if i != j:
        if(words[j].startswith(abbs[i]) == True):
          return False
  return True

