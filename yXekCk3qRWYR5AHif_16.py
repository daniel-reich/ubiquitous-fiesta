
def vow_replace(word, vowel):
  new_word = ''
  for c in word:
    if c in ['a', 'e', 'i', 'o', 'u']:
      new_word += vowel
    else:
      new_word += c
  return new_word

