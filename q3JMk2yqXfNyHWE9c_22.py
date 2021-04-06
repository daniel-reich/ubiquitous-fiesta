
def double_letters(word):
  for i in word:
    if i + i in word:
      return True
  return False

