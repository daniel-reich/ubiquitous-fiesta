
def unique_abbrev(abbs, words):
  k = 0
  while k < len(abbs):
    i = 0
    num = 0
    while i < len(words):
      if words[i].startswith(abbs[k]):
        num = num + 1
      if num > 1:
        return False
      i = i + 1
    k = k + 1
  return True

