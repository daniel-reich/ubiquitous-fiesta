
def hangman(phrase, lst):
  return ''.join(x if x.lower() in ''.join(lst)+' ,.!' or x.isdigit() else '-' for x in phrase)

