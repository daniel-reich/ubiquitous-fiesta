
def unstretch(word):
  return ''.join([x for x,y in zip(word,word[1:]) if x!=y]) + word[-1]

