
def get_middle(word):
  i = len(word)//2
  return word[i] if len(word)%2 else word[i-1:i+1]

