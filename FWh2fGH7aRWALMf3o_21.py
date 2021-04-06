
def cleaver(string, lst):
  if string in lst:
    return string
  for word in lst:
    if string[:len(word)]==word:
      cleaved = cleaver(string[len(word):],lst)
      if cleaved is not None:
        return word+" "+cleaved
  return None
​
def cleave(string, lst):
  cleaved = cleaver(string, lst)
  if cleaved is None:
    return "Cleaving stalled: Word not found"
  return cleaved

