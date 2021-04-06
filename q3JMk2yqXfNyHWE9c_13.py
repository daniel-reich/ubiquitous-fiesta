
def double_letters(word):
  return max([word[n] == word[n+1] for n in range(len(word)-1)])

