
def unstretch(word):
  new_word = ''
  last_letter = ''
  for letter in word:
    if letter != last_letter:
      new_word += letter
      last_letter = letter
  return new_word

