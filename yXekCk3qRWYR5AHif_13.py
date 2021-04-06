
def vow_replace(word, vowel):
  return "".join([l if l not in "aeiouAEIOU" else vowel for l in word])

