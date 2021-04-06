
def remove_letters(letters, word):
  for w in word:
    if w in letters:
      letters.remove(w)
  return letters

