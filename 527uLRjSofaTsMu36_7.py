
def get_middle(word):
  return word[len(word)//2] if len(word)%2==1 else word[len(word)//2-1:len(word)//2+1]

