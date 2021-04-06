
def hangman(phrase, lst):
  return ''.join(i if i.lower() in lst+list(" 1234567890.!") else "-" for i in phrase)

