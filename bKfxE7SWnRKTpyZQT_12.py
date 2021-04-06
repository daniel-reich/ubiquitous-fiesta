
def replace_vowel(word):
  x = "aeiou"
  return ''.join([i if i not in x else str(x.index(i)+1) for i in word])

