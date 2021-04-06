
def no_duplicate_letters(phrase):
  for i in phrase.split():
    for j in set(i):
      if i.count(j) >1:
        return False
  return True

