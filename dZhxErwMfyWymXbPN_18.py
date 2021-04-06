
def hangman(phrase, lst):
  return ''.join(i if (i.lower() in lst or not i.isalpha()) else '-' for i in phrase)

