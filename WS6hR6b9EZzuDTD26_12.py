
def no_duplicate_letters(phrase):
  for wrds in phrase.split():
    letter = ''
    for i in sorted(wrds):
      if(letter == i):
        return False
      else:
        letter = i
  return True

