
def retrieve(txt):
  return [''.join([c for c in word if c.isalpha()]) for word in txt.lower().split() if word[0] in "aeiou"]

