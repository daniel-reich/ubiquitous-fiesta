
def map_letters(word):
  return {i:find(i,word) for i in sorted(set(word), key=word.index)}
def find(i,word):
  return [k for k,j in enumerate(word) if j==i]

