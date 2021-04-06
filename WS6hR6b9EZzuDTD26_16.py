
def no_duplicate_letters(phrase):
  a=phrase.split()
  for i in a:
    for j in range(0,len(i)-1):
      if i[j] in i[j+1:]:
        return False
  return True

