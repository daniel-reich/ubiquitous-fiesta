
def vow_replace(word, vowel):
  cum = list(word)
  boom = []
  for x in cum:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
      boom.append(vowel)
    else:
      boom.append(x)
  return "".join(boom)

