
def get_middle(word):
  l = len(word)
  return "" if l==0 else word[l//2] if l%2 == 1 else word[l//2 - 1] + word[l//2]

