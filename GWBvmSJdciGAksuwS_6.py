
def find_letters(word):
  new_word = []
  for i in word:
    if word.count(i) == 1:
      new_word.append(i)
  return new_word

