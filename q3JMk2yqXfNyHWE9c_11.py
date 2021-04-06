
def double_letters(word):
  for i in range(len(word)):
    if i+1 != len(word):
      if word[i] == word[i+1]:
        return True
  return False

