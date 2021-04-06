
def hangman(phrase, lst):
  return "".join(c if c.lower() in lst or not c.isalpha() else "-" for c in phrase)

