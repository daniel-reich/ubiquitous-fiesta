
def replace_vowel(word):
  new_word = ""
  for w in word:
    if w in "aeiou":
      new_word += str("aeiou".index(w) + 1)
    else:
      new_word += w
  return new_word

