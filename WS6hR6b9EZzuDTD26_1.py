
def no_duplicate_letters(phrase):
  return all(i.count(j)==1 for i in phrase.split() for j in i)

