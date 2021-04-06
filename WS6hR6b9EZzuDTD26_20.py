
def no_duplicate_letters(phrase):
  phrase_list = phrase.split()
  counter = 0
  for words in phrase_list:
    for letters in words:
      counter = words.count(letters)
      if counter > 1:
        return False
  return True

