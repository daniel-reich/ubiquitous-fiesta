
def is_alpha(word):
  return sum([ord(x) for x in word.lower() if x.isalpha()])%2 == 0

