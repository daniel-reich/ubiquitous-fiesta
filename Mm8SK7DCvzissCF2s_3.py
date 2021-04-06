
def is_alpha(word):
  a = ' abcdefghijklmnopqrstuvwxyz'
  return sum([a.index(i) for i in word.lower() if i.isalpha()])%2 == 0

