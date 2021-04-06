
def vow_replace(word, vowel):
  return "".join([vowel if i in "aeiou" else i for i in word])

