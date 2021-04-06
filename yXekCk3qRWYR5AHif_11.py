
def vow_replace(word, vowel):
  return "".join(vowel if c in "aeiou" else c for c in word)

