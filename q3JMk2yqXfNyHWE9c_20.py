
def double_letters(word):
  return any([c == word[i+1] for i,c in enumerate(word) if i<len(word)-1])

