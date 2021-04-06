
def remove_letters(letters, word):
  for item in word:
    if item in letters:
      letters.remove(item)
  return letters

