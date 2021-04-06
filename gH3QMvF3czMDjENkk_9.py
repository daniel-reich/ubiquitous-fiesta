
def remove_letters(letters, word):
  l = letters
  for i in word:
    if i in l:
      l.remove(i)
  return l

