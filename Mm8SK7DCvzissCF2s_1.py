
def is_alpha(word):
  return sum(ord(c) for c in word if c.isalpha()) % 2 == 0

