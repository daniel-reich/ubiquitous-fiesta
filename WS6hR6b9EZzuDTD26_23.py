
def no_duplicate_letters(phrase):
  splitted_phrase=phrase.split()
  for i in splitted_phrase:
    for j,v in enumerate(sorted(i)):
      if j==len(sorted(i))-1:break
      if v==(sorted(i)[j+1]):
        return False
  return True

