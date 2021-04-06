
def remove_letters(letters, word):
  for letter in word:
    if letters.count(letter) > 0:
      letters.remove(letter)
  return letters

