
def double_letters(word):
  for c in word:
    if c*2 in word:
      return True
  return False

