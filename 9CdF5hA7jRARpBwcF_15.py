
def map_letters(word):
  return dict([[i,ind(i,word)] for i in word])
  
def ind(a,b):
  return [i for i in range(len(b)) if b[i]==a]

