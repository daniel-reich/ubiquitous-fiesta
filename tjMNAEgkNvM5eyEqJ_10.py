
def unique_abbrev(abbs, words):
  true_Count = 0
  for abbrev in abbs:
    for word in words:
      if word.startswith(abbrev):
        true_Count += 1
  if true_Count > 3:
    return False
  else:
    return True

