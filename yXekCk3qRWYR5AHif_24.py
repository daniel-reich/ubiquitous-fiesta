
def vow_replace(word, vowel):
  lst=["a","e","i","o","u"]
  for char in word:
    if char in lst:
      word=word.replace(char, vowel)
  return word

