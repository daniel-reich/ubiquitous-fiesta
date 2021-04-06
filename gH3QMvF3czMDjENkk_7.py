
def remove_letters(letters, word):
  for i in list(word):
    if i in letters:letters.remove(i)
  return letters

