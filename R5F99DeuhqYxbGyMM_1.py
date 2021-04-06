
def word_builder(ltr, pos):
  word=[]
  for i in pos:
    word.append(ltr[i])
  return ''.join(word)

