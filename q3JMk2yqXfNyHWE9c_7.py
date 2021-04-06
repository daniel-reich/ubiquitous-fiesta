
def double_letters(word):
  return (len([a for a in range(len(word)-1) if word[a]==word[a+1]])>0)

