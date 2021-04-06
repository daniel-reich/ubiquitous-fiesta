
def unique_abbrev(abbs, words):
  return len([j for i in range(len(words)) for j in range(len(abbs)) if words[i].startswith(abbs[j])]) == len(words)

