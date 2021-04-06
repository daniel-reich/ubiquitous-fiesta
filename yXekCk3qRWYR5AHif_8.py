
def vow_replace(word, vowel):
  return "".join([vowel if i in "aiueo" else i for i in word])

