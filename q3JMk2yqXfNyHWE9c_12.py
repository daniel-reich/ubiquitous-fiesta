
def double_letters(word):
  return any([word[i]==word[i+1] for i in range(len(word)-1)])

