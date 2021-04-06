
def double_letters(word):
  for i in range(1,len(word)):
    if word[i] == word[i-1]:
      return True
  return False

