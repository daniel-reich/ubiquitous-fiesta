
def remove_letters(letters, word):
  for c in word:
    if c in letters:
      letters.remove(c)
      
  return letters

