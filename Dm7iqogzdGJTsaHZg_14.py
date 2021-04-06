
def retrieve(txt):
  return [word.lower() for word in txt[:-1].split() if word[0].lower() in "aeiou"]

