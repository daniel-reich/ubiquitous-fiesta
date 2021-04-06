
def remove_letters(letters, word):
  for x in word:
    if x in letters:
      letters.remove(x)
  return letters

