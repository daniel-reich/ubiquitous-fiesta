
def in_alpha(word):
  return not sum(ord(c.lower()) - 96 for c in word if c.isalpha())%2

