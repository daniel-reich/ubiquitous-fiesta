
def double_letters(word):
  double = False
  i = 1
  while i < len(word):
    if word[i] == word[i-1]:
      double = True
      break
    i += 1
  return double

