
def retrieve(txt):
  return [word.strip('.') for word in txt.lower().split() if word[0] in 'aeiou']

