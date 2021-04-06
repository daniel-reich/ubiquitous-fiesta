
def remove_letters(letters, word):
  for letter in word:
    try:
        letters.remove(letter)
    except ValueError:
        continue
  return letters

