
def vow_replace(word, vowel):
  v = ['a', 'e', 'i', 'o', 'u']
  for letter in word:
    if letter in v:
      word = word.replace(letter, vowel)
  return word

