
def unique_abbrev(abbs, words):
  for i in abbs:
    count = 0
    for j in words:
      if j.startswith(i):
        count += 1
    if count > 1:
      return False
  return True

