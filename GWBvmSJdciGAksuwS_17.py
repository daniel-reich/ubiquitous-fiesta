
def find_letters(word):
  for l in word:
    if word.count(l) > 1:
      word = word.replace(l, "")
  word = " ".join(word)
  word = word.split()
  return word

