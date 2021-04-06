
def in_alpha(word):
  return not sum(ord(l) - 96 for l in word.lower() if l.isalpha()) % 2

