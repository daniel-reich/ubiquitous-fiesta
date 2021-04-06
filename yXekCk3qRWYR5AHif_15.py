
def vow_replace(word, vowel):
  new = ""
  for i in range(len(word)):
    if word[i].lower() in "aeiou":
      new += vowel
    else:
      new += word[i]
  return new

