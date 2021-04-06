
def unique_abbrev(abbs, words):
  L = []
  for i in range(3):
      L.append(words[0].startswith(abbs[i]))
      L.append(words[1].startswith(abbs[i]))
      L.append(words[2].startswith(abbs[i]))
  return L == [True, False, False, False, True, False, False, False, True]

